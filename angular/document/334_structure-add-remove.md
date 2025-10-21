# #334 「構造の追加・削除」

## 概要
Structural Directiveでは`ViewContainerRef`を使いテンプレートを挿入・削除することで、DOM構造を動的に制御する。

## 学習目標
- `createEmbeddedView`/`clear`の役割を理解する
- 差分更新を意識したビュー管理を学ぶ
- リソース解放のタイミングを把握する

## 技術ポイント
- `createEmbeddedView(template, context?)`でビューを挿入
- `remove()`/`clear()`で不要なビューを破棄
- EmbeddedViewRefを保持して再利用・更新を行うことも可能

## 📺 画面表示用コード（動画用）
```typescript
this.container.clear();
if (condition) this.container.createEmbeddedView(this.template);
```

## 💻 詳細実装例（学習用）
```typescript
@Directive({
  selector: '[appToggleView]',
  standalone: true
})
export class ToggleViewDirective implements OnChanges, OnDestroy {
  @Input({ alias: 'appToggleView', required: true }) active!: boolean;
  private currentView?: EmbeddedViewRef<unknown>;

  constructor(private readonly container: ViewContainerRef, private readonly template: TemplateRef<unknown>) {}

  ngOnChanges(): void {
    if (this.active) {
      if (!this.currentView) {
        this.currentView = this.container.createEmbeddedView(this.template);
      }
    } else {
      this.container.clear();
      this.currentView = undefined;
    }
  }

  ngOnDestroy(): void {
    this.container.clear();
  }
}

@Component({
  selector: 'app-toggle-view-demo',
  standalone: true,
  imports: [CommonModule, ToggleViewDirective],
  template: `
    <label>
      <input type="checkbox" [(ngModel)]="checked" />
      表示をトグル
    </label>
    <section *appToggleView="checked">切り替え対象</section>
  `
})
export class ToggleViewDemoComponent {
  protected checked = false;
}
```

## ベストプラクティス
- ビュー生成後は参照を保持して不要な再生成を避ける
- `clear`と`remove`の使い分けを理解し、特定インデックスだけ削除できるようにする
- `ngOnDestroy`で必ずビューを破棄し、メモリリークを防ぐ

## 注意点
- 頻繁な生成・削除はパフォーマンスに影響するため、条件式の変化頻度を抑える
- 破棄忘れでObservable購読が残るのを避けるため、EmbeddedView内の`onDestroy`を活用する
- SSRではViewContainerRefがDOM操作を行わないため、副作用を限定する

## 関連技術
- EmbeddedViewRef
- Lifecycle Hooks
- Angular Forms (例内で使用)
