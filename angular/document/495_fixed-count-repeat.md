# #495 「指定回数の繰り返し表示」

## 概要
指定回数の繰り返し表示はInputで受け取った数値分だけビューを生成し、単純な反復処理をテンプレート上で簡潔に記述できる。

## 学習目標
- count値に応じたビュー生成ロジックを理解する
- 入力値のバリデーションとクレンジング方法を学ぶ
- 再レンダリング時の処理フローを把握する

## 技術ポイント
- `Math.max(0, Math.floor(count))`で正規化
- ViewContainerRefをclear後にループでcreateEmbeddedView
- Contextにインデックスやその他情報を提供

## 📺 画面表示用コード（動画用）
```typescript
const times = Math.max(0, Math.floor(this.count));
```

## 💻 詳細実装例（学習用）
```typescript
@Directive({
  selector: '[appRepeat]',
  standalone: true
})
export class RepeatDirective implements OnChanges {
  @Input('appRepeat') count = 0;

  constructor(
    private readonly template: TemplateRef<{ $implicit: number; index: number }>,
    private readonly viewContainer: ViewContainerRef
  ) {}

  ngOnChanges(): void {
    this.viewContainer.clear();
    const times = Math.max(0, Math.floor(this.count));
    for (let i = 0; i < times; i++) {
      this.viewContainer.createEmbeddedView(this.template, { $implicit: i, index: i });
    }
  }
}
```

## ベストプラクティス
- countが負数や非数の場合のフォールバックを実装
- Contextに`first`/`last`/`even`などのフラグも提供すると便利
- count変更時は多くのビューが更新されるため必要に応じ最適化

## 注意点
- 回数が大きいとDOMが膨大になるためサーバーサイドレンダリングとの兼ね合いに注意
- 変更差分が大きくなる場合は手動でremove/insertする最適化も検討
- 同じ要素に他のStructural Directiveを付けられないルールを理解

## 関連技術
- ViewContainerRef
- Contextオブジェクト
- Structural Directive基礎
