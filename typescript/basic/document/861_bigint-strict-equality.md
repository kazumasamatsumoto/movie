# #861 「等価比較 - ===」

四国めたん「bigint同士の等価比較は===で行います。」
ずんだもん「numberと同じ演算子なんだね。」
四国めたん「型も値も一致する場合だけtrueです。」
ずんだもん「同じ値なら別々に生成したBigIntでもtrueになるよ。」
四国めたん「ただしnumberと比較するとfalseになります。」
ずんだもん「===で型も含めて比較する癖を付けよう！」
四国めたん「精度を守るために厳密比較を標準にしましょう。」
ずんだもん「BigIntの等価比較は===が基本だよ！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 同値 */
console.log(10n === 10n); // true

/** Example 2: 異なる型 */
console.log(10n === 10); // false

/** Example 3: 比較関数 */
function isSame(a: bigint, b: bigint) {
  return a === b;
}
```
