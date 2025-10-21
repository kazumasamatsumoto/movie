# #498 「開始・終了の指定」

## 概要
Rangeディレクティブでは開始値（from）と終了値（to）をInputとして受け取り、ループ条件を決定する。stepも合わせて指定すると柔軟な範囲反復が可能になる。

## 学習目標
- 範囲指定に必要なInputの設計を理解する
- from/to/stepの関係を把握する
- 入力値のバリデーション方法を学ぶ

## 技術ポイント
- `@Input('appRangeFrom')`, `@Input('appRangeTo')`, `@Input('appRangeStep')`
- from > toの場合はstepの符号を反転
- stepが0のときはエラーを投げるかデフォルト値を適用

## 📺 画面表示用コード（動画用）
```typescript
const increasing = this.to >= this.from;
const step = increasing ? Math.abs(this.step) : -Math.abs(this.step);
```

## 💻 詳細実装例（学習用）
```typescript
@Directive({
  selector: '[appRange]',
  standalone: true
})
export class RangeDirective implements OnChanges {
  @Input('appRangeFrom') from = 0;
  @Input('appRangeTo') to = 0;
  @Input('appRangeStep') step = 1;

  // ...（497の実装と同様）
}
```

## ベストプラクティス
- Inputにデフォルト値を設定し、undefinedでも安全に動作
- from/to/stepの組み合わせが不正な場合はエラーや警告を出す
- 範囲が広い場合はユーザーへ注意を促す

## 注意点
- stepの符号を調整しないと無限ループになる可能性
- Number以外が渡された場合は型チェックを行う
- 小数ステップを扱う場合は浮動小数の誤差に注意

## 関連技術
- RangeDirective
- TemplateRef / ViewContainerRef
- Structural Directive Input設計
