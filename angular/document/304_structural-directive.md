# #304 「Structural Directive - 構造ディレクティブ」

## 概要
Structural Directiveはテンプレートの生成と破棄を管理し、条件やコレクションに応じてDOM構造そのものを差し替える機能を提供する。

## 学習目標
- Structural DirectiveがDOM構造に与える影響を理解する
- TemplateRefとViewContainerRefの役割を把握する
- 条件付きレンダリングを行うカスタム構造ディレクティブを実装する

## 技術ポイント
- `@Directive`と属性セレクタで`*`構文を提供
- `ViewContainerRef`で埋め込みビューを生成・破棄
- `@Input`エイリアスで直感的なAPIを設計

## 📺 画面表示用コード（動画用）
```typescript
@Directive({ selector: '[appIfRole]', standalone: true })
export class IfRoleDirective implements OnChanges {
  @Input({ alias: 'appIfRole', required: true }) role!: string;
  constructor(private view: ViewContainerRef, private tpl: TemplateRef<unknown>, private auth: AuthService) {}
  ngOnChanges(): void {
    this.view.clear();
    if (this.auth.hasRole(this.role)) this.view.createEmbeddedView(this.tpl);
  }
}
```

## 💻 詳細実装例（学習用）
```typescript
@Injectable({ providedIn: 'root' })
export class AuthService {
  private readonly roles = signal<string[]>(['reader', 'editor']);
  hasRole(role: string): boolean {
    return this.roles().includes(role);
  }
}

@Directive({
  selector: '[appIfRole]',
  standalone: true
})
export class IfRoleDirective implements OnChanges, OnDestroy {
  @Input({ alias: 'appIfRole', required: true }) role!: string;
  private embedded?: EmbeddedViewRef<unknown>;

  constructor(
    private readonly view: ViewContainerRef,
    private readonly template: TemplateRef<unknown>,
    private readonly auth: AuthService
  ) {}

  ngOnChanges(): void {
    this.view.clear();
    this.embedded = undefined;
    if (this.auth.hasRole(this.role)) {
      this.embedded = this.view.createEmbeddedView(this.template);
    }
  }

  ngOnDestroy(): void {
    this.embedded?.destroy();
  }
}

@Component({
  selector: 'app-if-role-demo',
  standalone: true,
  imports: [CommonModule, IfRoleDirective],
  template: `
    <p *appIfRole="'editor'">編集者だけが見えるブロックです。</p>
    <p *appIfRole="'admin'">管理者限定コンテンツ。</p>
  `
})
export class IfRoleDemoComponent {}
```

## ベストプラクティス
- 初期化とクリーンアップで`ViewContainerRef.clear()`を確実に呼び、ビューの重複を防ぐ
- 受け取るパラメータは`@Input`エイリアスを活用し、読みやすい`*appX="条件"`構文を提供する
- 大規模なテンプレートではメモリ使用量に注意し、不要なビューを即座に破棄する

## 注意点
- 条件が頻繁に変わる場合、毎回新規ビューを作らず差分更新を検討する
- `TemplateRef`への依存をテストでモックし、埋め込みビューの生成を検証する
- SSRでは初期の表示状態をブラウザと揃え、ハイドレーションエラーを避ける

## 関連技術
- TemplateRef
- EmbeddedViewRef
- Structural Directives (`*ngIf`, `@for`)
