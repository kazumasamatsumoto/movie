# #878 「Math.pow()とべき乗」

四国めたん「Math.powもbigintには対応していません。」
ずんだもん「代わりに**演算子を使えばいいんだね。」
四国めたん「はい、BigIntの指数もBigIntで指定します。」
ずんだもん「負の指数や小数は使えないから注意しよう。」
四国めたん「大きなべき乗はコストが高いので繰り返し二乗法など最適化を考えましょう。」
ずんだもん「Math.powの代替として演算子や専用関数を押さえてね！」
四国めたん「アルゴリズムに合わせて使い分けてください。」
ずんだもん「BigIntのべき乗で制約を乗り越えよう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: Math.powは不可 */
// Math.pow(2n, 10n); // コンパイル・実行ともにエラー

/** Example 2: **演算子 */
const power = 2n ** 10n;

/** Example 3: ユーティリティ */
function pow(base: bigint, exponent: bigint): bigint {
  if (exponent < 0n) throw new Error("negative exponent not supported");
  let result = 1n;
  let b = base;
  let e = exponent;
  while (e > 0n) {
    if (e & 1n) result *= b;
    e >>= 1n;
    b *= b;
  }
  return result;
}
```
