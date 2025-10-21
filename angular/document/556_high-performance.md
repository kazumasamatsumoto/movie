# #556 「パフォーマンスが高い」

## 概要
純粋Pipeは入力参照が変わったときだけ再評価されるため、重い処理でも変更検知のたびに実行されずパフォーマンスに優れる。

## 学習目標
- 純粋Pipeがパフォーマンスへ与えるメリットを理解する
- 再評価頻度を抑える設計を学ぶ
- 重い処理をPipeに閉じ込める際の注意点を把握する

## 技術ポイント
- `pure: true`で参照変更時のみ再評価
- 重い計算やフォーマット処理をPipeに委ねるとテンプレートがシンプルに
- 参照を変えない更新では再描画されない

## 📺 画面表示用コード（動画用）
```html
<p>{{ heavyValue | heavyCalculation }}</p>
```

## 💻 詳細実装例（学習用）
```typescript
@Pipe({ name: 'heavyCalculation', standalone: true })
export class HeavyCalculationPipe implements PipeTransform {
  transform(value: number): number {
    // 高コストな処理があってもpureなら参照が変わったときだけ実行
    return expensiveComputation(value);
  }
}
```

## ベストプラクティス
- 高コストな処理はPurePipeにし、参照に基づく再評価制御を活用
- 入力値の参照が変わるようimmutable更新を行う
- パフォーマンスが問題になる場合はProfilerで評価

## 注意点
- mutableなデータを直接変更すると更新されない
- Pipe内で非同期処理を書くのは避ける
- Inputが頻繁に変わる場合は依然として再評価が起きる

## 関連技術
- Impure Pipe
- Change Detection
- Performance Profiling
