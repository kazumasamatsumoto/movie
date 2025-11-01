# #844 「除算 - a / b」

四国めたん「bigintの除算は/演算子で行い、結果は整数に切り捨てられます。」
ずんだもん「余りはどうするの？」
四国めたん「%演算子で取得します。小数は扱えないので商は常に整数です。」
ずんだもん「金融の割り勘みたいに余りも考慮して処理したいね。」
四国めたん「ゼロ除算は相変わらずエラーになります。」
ずんだもん「BigIntの除算で安全な整数計算をしよう！」
四国めたん「商と余りをペアで扱うユーティリティを用意すると便利です。」
ずんだもん「丸めエラーが出ないのが安心だよ！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 基本除算 */
const quotient = 10n / 3n; // 3n

/** Example 2: 商と余り */
function divmod(a: bigint, b: bigint) {
  return { q: a / b, r: a % b };
}

/** Example 3: 割り勘 */
const total = 100n;
const people = 3n;
const { q, r } = divmod(total, people);
```
