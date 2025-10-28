# #864 「大小比較 - <, >, <=, >=」

四国めたん「bigintの大小比較も<や>などの演算子が使えます。」
ずんだもん「numberと同じ感じで比較できるんだね。」
四国めたん「厳密比較と同様に型を揃えて扱いましょう。」
ずんだもん「巨大な差分でも正確に判定できるのが強いよ。」
四国めたん「<=や>=を使えば範囲チェックも簡単です。」
ずんだもん「BigIntの大小比較で制御フローを組み立てよう！」
四国めたん「比較は常に整数精度で行われます。」
ずんだもん「安心して閾値を設定できるね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 比較 */
console.log(1000n > 999n);

/** Example 2: 範囲チェック */
function withinRange(value: bigint, min: bigint, max: bigint) {
  return value >= min && value <= max;
}

/** Example 3: 条件分岐 */
if (withinRange(500n, 100n, 1000n)) {
  console.log("ok");
}
```
