# #481 「カスタム Structural Directive の作成」

## 概要
カスタムStructural Directiveはテンプレートの生成・破棄を制御する仕組みで、`TemplateRef`と`ViewContainerRef`を使ってDOMツリーを動的に構築できる。

## 学習目標
- Structural Directiveの基本構造を理解する
- TemplateRefとViewContainerRefの役割を学ぶ
- *構文を有効にするためのselector設計を把握する

## 技術ポイント
- `@Directive({ selector: '[appUnless]', standalone: true })`
- `constructor(private template: TemplateRef<unknown>, private view: ViewContainerRef)`
- `createEmbeddedView`/`clear`でビューを生成・破棄

## 📺 画面表示用コード（動画用）
```typescript
constructor(private tpl: TemplateRef<unknown>, private vc: ViewContainerRef) {}
```

## 💻 詳細実装例（学習用）
```typescript
@Directive({
  selector: '[appUnless]',
  standalone: true
})
export class UnlessDirective implements OnChanges {
  @Input('appUnless') condition = false;
  private hasView = false;

  constructor(
    private readonly template: TemplateRef<unknown>,
    private readonly viewContainer: ViewContainerRef
  ) {}

  ngOnChanges(): void {
    if (!this.condition && !this.hasView) {
      this.viewContainer.createEmbeddedView(this.template);
      this.hasView = true;
    } else if (this.condition && this.hasView) {
      this.viewContainer.clear();
      this.hasView = false;
    }
  }
}
```

## ベストプラクティス
- ビュー生成状況をフラグで保持し、不要な再生成を避ける
- Inputエイリアスで`*appUnless`のような構文を提供
- コンテキストが必要な場合は`createEmbeddedView`の第二引数に渡す

## 注意点
- Structural Directiveは同一要素に複数付与できないため設計時に意識
- TemplateRef/ViewContainerRefはコンストラクタ注入のみ可能
- ビュー破棄漏れがないよう条件分岐を明確に

## 関連技術
- TemplateRef
- ViewContainerRef
- Structural Directiveテンプレート構文
