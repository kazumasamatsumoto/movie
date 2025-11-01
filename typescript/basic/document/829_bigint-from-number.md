# #829 「BigInt()関数 - 数値」

四国めたん「BigInt関数にnumberを渡すと整数部分だけがbigintになります。」
ずんだもん「小数を渡すとどうなるの？」
四国めたん「RangeErrorになります。整数であることが前提です。」
ずんだもん「Number.MAX_SAFE_INTEGERを超える前にBigIntへ変換したいね。」
四国めたん「bigintリテラルが使えない動的値はBigInt(number)で変換します。」
ずんだもん「暗号ハッシュの一部をBigIntにするときにも活躍するよ。」
四国めたん「入力値の確認を行い、安全に変換しましょう。」
ずんだもん「数値からBigIntへスマートに変換しよう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: numberから変換 */
const fromNumber = BigInt(9007199254740991);

/** Example 2: RangeError */
try {
  BigInt(1.5);
} catch (error) {
  console.error(error); // RangeError
}

/** Example 3: ガード付き変換 */
function toBigInt(value: number): bigint {
  if (!Number.isInteger(value)) throw new Error("integer required");
  return BigInt(value);
}
```
