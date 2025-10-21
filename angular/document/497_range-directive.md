# #497 「Range Directive - 範囲指定」

## 概要
Rangeディレクティブは開始値と終了値を指定して数値範囲を反復し、テンプレートに範囲内の値を提供する構造ディレクティブである。

## 学習目標
- 数値範囲を扱う構造ディレクティブの設計を理解する
- `from`/`to`/`step`などのInput設計を学ぶ
- ViewContainerRefで範囲内の値を順次生成する方法を把握する

## 技術ポイント
- `@Input() appRangeFrom`, `@Input() appRangeTo`, `@Input() appRangeStep`
- ループで`createEmbeddedView`を呼んで値を渡す
- stepの符号と終了条件を考慮

## 📺 画面表示用コード（動画用）
```html
<li *appRange="let n from 1 to 5">{{ n }}</li>
```

## 💻 詳細実装例（学習用）
```typescript
interface RangeContext {
  $implicit: number;
  index: number;
}

@Directive({
  selector: '[appRange]',
  standalone: true
})
export class RangeDirective implements OnChanges {
  @Input('appRangeFrom') from = 0;
  @Input('appRangeTo') to = 0;
  @Input('appRangeStep') step = 1;

  constructor(
    private readonly template: TemplateRef<RangeContext>,
    private readonly viewContainer: ViewContainerRef
  ) {}

  ngOnChanges(): void {
    this.viewContainer.clear();
    if (this.step === 0) {
      throw new Error('appRangeStep must not be 0');
    }
    const increasing = this.to >= this.from;
    const effectiveStep = increasing ? Math.abs(this.step) : -Math.abs(this.step);
    let index = 0;
    for (let value = this.from; increasing ? value <= this.to : value >= this.to; value += effectiveStep) {
      this.viewContainer.createEmbeddedView(this.template, { $implicit: value, index });
      index++;
    }
  }
}
```

## ベストプラクティス
- stepが0の場合はエラーとし、利用者へ明確に伝える
- 範囲が逆（from > to）の場合はstep符号を自動調整
- Contextでindexや`first`/`last`なども提供可能

## 注意点
- 大きな範囲を生成するとDOMが肥大化するため上限をドキュメント化
- SSRでも同じ結果になるよう同期処理で実装
- Input更新時に前のビューを必ずclearする

## 関連技術
- TemplateRef
- ViewContainerRef
- Contextオブジェクト
