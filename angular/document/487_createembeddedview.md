# #487 「createEmbeddedView() メソッド」

## 概要
`createEmbeddedView()`はTemplateRefからビューを生成してViewContainerRefに挿入するメソッドで、コンテキストを渡すことでテンプレートへ値を供給できる。

## 学習目標
- createEmbeddedViewの引数と戻り値を理解する
- コンテキストオブジェクトの渡し方を学ぶ
- 生成したビューを保持して再利用するケースを把握する

## 技術ポイント
- `createEmbeddedView(template, context?, index?)`
- 戻り値は`EmbeddedViewRef`
- コンテキストで`$implicit`や他のプロパティを提供

## 📺 画面表示用コード（動画用）
```typescript
const view = this.viewContainer.createEmbeddedView(this.template, { $implicit: item });
```

## 💻 詳細実装例（学習用）
```typescript
interface RepeatContext<T> {
  $implicit: T;
  index: number;
}

@Directive({
  selector: '[appRepeat]',
  standalone: true
})
export class RepeatDirective<T> implements OnChanges {
  @Input('appRepeat') count = 0;
  @Input('appRepeatOf') value!: T;

  constructor(private readonly template: TemplateRef<RepeatContext<T>>, private readonly viewContainer: ViewContainerRef) {}

  ngOnChanges(): void {
    this.viewContainer.clear();
    for (let i = 0; i < this.count; i++) {
      this.viewContainer.createEmbeddedView(this.template, {
        $implicit: this.value,
        index: i
      });
    }
  }
}
```

## ベストプラクティス
- コンテキストを明示的に定義してテンプレート側の型安全性を確保
- 生成した`EmbeddedViewRef`を必要に応じて配列で保持しておく
- index引数を使うと挿入位置を細かく制御できる

## 注意点
- 同じテンプレートから複数ビューを生成する場合は不要なclearを避ける
- 生成後にビューが不要になったら`remove`/`clear`で破棄しないとメモリリーク
- コンテキストのプロパティ名はテンプレートの`let`宣言と一致させる

## 関連技術
- TemplateRef
- ViewContainerRef
- EmbeddedViewRef
