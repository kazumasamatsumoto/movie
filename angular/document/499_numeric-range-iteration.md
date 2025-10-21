# #499 「数値範囲の反復」

## 概要
数値範囲の反復では指定したfrom/to/stepに従って数値を生成し、テンプレートへ渡して繰り返し表示する。範囲方向に応じてループ条件を制御することが重要。

## 学習目標
- 数値範囲ループのロジックを理解する
- stepの方向と終了条件の決定方法を学ぶ
- Contextオブジェクトでブールフラグ（first/last等）を提供する

## 技術ポイント
- 増加方向か減少方向かを判定
- forループで`value += effectiveStep`
- last/firstフラグを計算してContextに追加

## 📺 画面表示用コード（動画用）
```typescript
for (let value = from, index = 0; increasing ? value <= to : value >= to; value += step, index++) { ... }
```

## 💻 詳細実装例（学習用）
```typescript
interface RangeContext {
  $implicit: number;
  index: number;
  first: boolean;
  last: boolean;
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
      throw new Error('step must not be 0');
    }
    const increasing = this.to >= this.from;
    const step = increasing ? Math.abs(this.step) : -Math.abs(this.step);
    const values: number[] = [];
    for (let value = this.from; increasing ? value <= this.to : value >= this.to; value += step) {
      values.push(value);
    }
    values.forEach((value, index) => {
      this.viewContainer.createEmbeddedView(this.template, {
        $implicit: value,
        index,
        first: index === 0,
        last: index === values.length - 1
      });
    });
  }
}
```

## ベストプラクティス
- コンテキストにindex/first/lastなど補助情報を提供
- 範囲が大きい場合でも性能に注意し、必要なら仮想スクロールを検討
- stepの絶対値が小さいとループ回数が増えるため注意喚起

## 注意点
- 浮動小数ステップで終端が一致しない場合があるので丸め処理を検討
- 逆方向ループでstep符号を誤ると無限ループ
- ループ後にViewRef参照を保持する場合は破棄を忘れない

## 関連技術
- TemplateRef/Context
- ViewContainerRef
- RangeDirective
