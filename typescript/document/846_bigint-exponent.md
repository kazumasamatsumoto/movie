# #846 「べき乗 - a ** b」

四国めたん「bigintのべき乗は**演算子が利用できます。」
ずんだもん「指数もbigintで指定するんだね。」
四国めたん「はい、負の指数はサポートされないので注意してください。」
ずんだもん「巨大なべき乗は急激に桁数が増えるからパフォーマンスに気を付けよう。」
四国めたん「必要に応じて累乗モジュラー演算を使うと効率的です。」
ずんだもん「BigIntでべき乗を扱うテクを身につけよう！」
四国めたん「数論や暗号に欠かせない演算です。」
ずんだもん「指数演算を安全に実装してね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 基本べき乗 */
const power = 2n ** 10n; // 1024n

/** Example 2: 巨大べき乗 */
const hugePow = 10n ** 50n;

/** Example 3: 繰り返し二乗法 */
function pow(base: bigint, exponent: bigint, mod?: bigint): bigint {
  let result = 1n;
  let b = mod ? base % mod : base;
  let e = exponent;
  while (e > 0n) {
    if (e & 1n) {
      result = mod ? (result * b) % mod : result * b;
    }
    e >>= 1n;
    b = mod ? (b * b) % mod : b * b;
  }
  return result;
}
```
