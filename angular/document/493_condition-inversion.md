# #493 「条件の反転実装」

## 概要
条件反転実装ではInputで受け取ったtruthy値を否定し、falseの場合のみテンプレートを生成する。null/undefinedなど特殊値への対応が重要。

## 学習目標
- 条件反転の実装テクニックを理解する
- truthy/falsyの扱いを学ぶ
- Inputをsetterで処理するパターンを把握する

## 技術ポイント
- boolean化してから反転（`!coerceBooleanProperty(value)`など）
- `null`や`undefined`をfalseとして扱う
- `SimpleChanges`を利用した変化検知も選択肢

## 📺 画面表示用コード（動画用）
```typescript
set appUnless(value: unknown) { const condition = coerceBooleanProperty(value); ... }
```

## 💻 詳細実装例（学習用）
```typescript
@Directive({
  selector: '[appUnless]',
  standalone: true
})
export class UnlessDirective {
  private hasView = false;

  constructor(
    private readonly template: TemplateRef<unknown>,
    private readonly viewContainer: ViewContainerRef
  ) {}

  @Input('appUnless')
  set condition(value: unknown) {
    const shouldHide = coerceBooleanProperty(value);
    if (!shouldHide && !this.hasView) {
      this.viewContainer.createEmbeddedView(this.template);
      this.hasView = true;
    } else if (shouldHide && this.hasView) {
      this.viewContainer.clear();
      this.hasView = false;
    }
  }
}
```

## ベストプラクティス
- `@angular/cdk/coercion` の `coerceBooleanProperty` を利用し真偽値判定を統一
- 反転結果を明確な変数に格納し読みやすくする
- 条件が変化した際にのみビュー操作を行う

## 注意点
- 文字列や数値もtruthy/falsyを期待通りに扱うためドキュメント化
- `null`をfalse扱いする場合とエラーにする場合を要件に合わせて設計
- 型安全性を保つためInputの型を可能ならbooleanに限定

## 関連技術
- coerceBooleanProperty
- TemplateRef/ViewContainerRef
- Structural DirectiveのInputハンドリング
