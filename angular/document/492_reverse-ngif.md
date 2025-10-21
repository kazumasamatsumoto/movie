# #492 「*ngIf の逆の動作」

## 概要
`*ngIf`の逆動作を提供するUnlessディレクティブは、条件がfalseのときだけビューを表示する。否定条件をテンプレートでわかりやすく表現できる。

## 学習目標
- `*ngIf`の逆動作を実装するロジックを理解する
- Input setterで条件変化を監視する手法を学ぶ
- ビュー生成と破棄のパターンを把握する

## 技術ポイント
- `set condition(value: boolean)`でtrueならclear、falseならcreate
- `coerceBooleanProperty`などで値をboolean化
- 再生成を避けるため`hasView`フラグを使う

## 📺 画面表示用コード（動画用）
```html
<div *appUnless="form.valid">フォームを入力してください</div>
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
  set appUnless(condition: boolean) {
    if (!condition && !this.hasView) {
      this.viewContainer.createEmbeddedView(this.template);
      this.hasView = true;
    } else if (condition && this.hasView) {
      this.viewContainer.clear();
      this.hasView = false;
    }
  }
}
```

## ベストプラクティス
- `hasView`でビュー重複を防ぎ、パフォーマンスを維持
- negated条件をテンプレートに書かずに済むので可読性が向上
- Inputエイリアスでテンプレート内のバインディング名を揃える

## 注意点
- 条件が変更されるたびにビュー操作が走るため、不要な変更を避ける
- `null`や`undefined`の扱いを統一し、ドキュメントに記載
- `*appUnless; else`のような構文は自作で対応するか検討

## 関連技術
- `*ngIf`
- TemplateRef / ViewContainerRef
- Structural DirectiveのInput setter
