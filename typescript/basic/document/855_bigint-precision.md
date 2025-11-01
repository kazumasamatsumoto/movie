# #855 「演算の精度」

四国めたん「bigintの演算は常に整数精度を保ちます。」
ずんだもん「numberみたいに浮動小数点の丸め誤差が出ないんだね。」
四国めたん「その代わり小数は扱えません。」
ずんだもん「精度重視の場面ではBigIntで演算したあと必要ならnumberへ変換しよう。」
四国めたん「計算過程もすべて整数で書くと品質が上がります。」
ずんだもん「精度のコントロールを理解してBigIntを選択しよう！」
四国めたん「演算結果が確実に正しいという安心感が得られます。」
ずんだもん「精度重視の計算はBigIntに任せよう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: numberの誤差 */
const floatSum = 0.1 + 0.2;

/** Example 2: bigintで精度保持 */
const preciseSum = (1n + 2n) * 1000000000000000000n;

/** Example 3: 比較 */
console.log(floatSum === 0.3); // false
console.log(preciseSum === 3n * 1000000000000000000n); // true
```
