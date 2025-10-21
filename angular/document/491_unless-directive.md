# #491 「Unless Directive - 反転条件」

## 概要
Unlessディレクティブは条件がfalseのときにテンプレートを表示する構造ディレクティブで、`*ngIf`の反転版として読みやすいテンプレート構文を提供する。

## 学習目標
- Unlessディレクティブの動作を理解する
- 条件の反転を`createEmbeddedView`/`clear`で実装する方法を学ぶ
- `*appUnless`構文で利用できるようselectorとInputエイリアスを設定する

## 技術ポイント
- `@Input('appUnless') set condition(value: boolean)`
- `value === false`時にビュー生成、trueで`clear`
- `this.hasView`フラグで二重生成を防止

## 📺 画面表示用コード（動画用）
```html
<p *appUnless="isLoggedIn">ログインしてください</p>
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
  set condition(value: boolean) {
    if (!value && !this.hasView) {
      this.viewContainer.createEmbeddedView(this.template);
      this.hasView = true;
    } else if (value && this.hasView) {
      this.viewContainer.clear();
      this.hasView = false;
    }
  }
}
```

## ベストプラクティス
- フラグを持って不要なcreateEmbeddedViewを防ぐ
- `*appUnless="items?.length"`のようにnull安全な式を推奨
- 真偽値以外の値でも正しく動作するようcoerceすることも検討

## 注意点
- `condition`がundefinedの場合の扱いを明確にする
- ビューを保持しないため毎回clearすると生成コストがかかる
- `appUnless`と`ngIf`を同じ要素で併用できない

## 関連技術
- TemplateRef/ViewContainerRef
- Structural DirectiveのInputエイリアス
- `*ngIf`との比較
