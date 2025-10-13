# #897 「組み合わせ計算」

四国めたん「組み合わせ数や階乗はBigIntが得意分野です。」
ずんだもん「nCkや多重階乗はすぐに桁あふれするから助かるね。」
四国めたん「はい、TypeScriptで汎用的なnCk関数を実装してみましょう。」
ずんだもん「動的計画法やPascalの三角形もBigIntなら精度バッチリだよ。」
四国めたん「大規模な統計計算にも応用できます。」
ずんだもん「組み合わせ計算でBigIntを活かして正確な結果を得よう！」
四国めたん「計算量に合わせてアルゴリズムも最適化してください。」
ずんだもん「数学的処理が安心して書けるね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 階乗 */
function factorial(n: bigint): bigint {
  let result = 1n;
  for (let i = 2n; i <= n; i++) {
    result *= i;
  }
  return result;
}

/** Example 2: nCk */
function combination(n: bigint, k: bigint): bigint {
  if (k > n) return 0n;
  if (k === 0n || k === n) return 1n;
  let numerator = 1n;
  let denominator = 1n;
  for (let i = 1n; i <= k; i++) {
    numerator *= n - (i - 1n);
    denominator *= i;
  }
  return numerator / denominator;
}

/** Example 3: 使用 */
console.log(combination(50n, 6n));
```
