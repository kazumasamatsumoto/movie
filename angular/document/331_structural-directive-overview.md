# #331 「Structural Directive とは？」

## 概要
Structural DirectiveはAngularテンプレートのDOM構造を動的に変更し、要素の追加・削除や条件分岐を行うディレクティブの総称である。

## 学習目標
- Structural Directiveの役割と特徴を説明できる
- DOM構造を操作するメリットと注意点を理解する
- 代表的なディレクティブへの導入として位置づけを把握する

## 技術ポイント
- `TemplateRef`と`ViewContainerRef`でテンプレートを生成・破棄
- `*`構文は`<ng-template>`への糖衣構文
- 代表例: `*ngIf`, `*ngFor`, `*ngSwitch`, カスタムStructural Directive

## 📺 画面表示用コード（動画用）
```typescript
@Directive({ selector: '[appVisible]' })
export class VisibleDirective {}
```

## 💻 詳細実装例（学習用）
```typescript
@Directive({
  selector: '[appVisible]',
  standalone: true
})
export class VisibleDirective implements OnChanges {
  @Input({ alias: 'appVisible', required: true }) visible!: boolean;

  constructor(private readonly view: ViewContainerRef, private readonly template: TemplateRef<unknown>) {}

  ngOnChanges(): void {
    this.view.clear();
    if (this.visible) {
      this.view.createEmbeddedView(this.template);
    }
  }
}

@Component({
  selector: 'app-visible-demo',
  standalone: true,
  imports: [CommonModule, VisibleDirective],
  template: `
    <button type="button" (click)="toggle()">切り替え</button>
    <p *appVisible="state">表示中の要素</p>
  `
})
export class VisibleDemoComponent {
  protected state = true;
  protected toggle(): void {
    this.state = !this.state;
  }
}
```

## ベストプラクティス
- DOM構造の責務に集中させ、ビジネスロジックはサービスへ委譲する
- `Renderer2`を併用し直接DOM操作を避ける
- テストで生成されるビュー数や条件分岐を検証し、予期せぬ表示崩れを防ぐ

## 注意点
- 頻繁な生成・破棄はコストになるため差分更新を意識する
- SSR環境ではDOMが存在しないため、`isPlatformBrowser`でガードする
- 複雑なネストは可読性が落ちるのでテンプレートを分割する

## 関連技術
- TemplateRef / ViewContainerRef
- Renderer2
- Angular Change Detection
