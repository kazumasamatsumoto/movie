# #877 「Math.sqrt()のbigint版」

四国めたん「bigint用の平方根は自前で実装するかライブラリを使います。」
ずんだもん「整数平方根を返すアルゴリズムが必要なんだね。」
四国めたん「二分探索やニュートン法で実装できます。」
ずんだもん「TypeScriptならジェネリクスなしでbigint専用関数を書けばいいよ。」
四国めたん「余りを返すバリエーションもあると便利です。」
ずんだもん「Math.sqrtが使えない制約を補うテクを覚えよう！」
四国めたん「精度を保ちながら平方根を求められます。」
ずんだもん「bigint向けsqrtで数論計算を支援しよう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 整数平方根(二分探索) */
function bigintSqrt(value: bigint): bigint {
  if (value < 0n) throw new Error("negative");
  if (value < 2n) return value;
  let low = 1n;
  let high = value;
  while (low <= high) {
    const mid = (low + high) >> 1n;
    const sq = mid * mid;
    if (sq === value) return mid;
    if (sq < value) low = mid + 1n;
    else high = mid - 1n;
  }
  return high;
}

/** Example 2: 余り付き */
function sqrtRem(value: bigint) {
  const root = bigintSqrt(value);
  return { root, remainder: value - root * root };
}

/** Example 3: 使用 */
console.log(sqrtRem(144n));
```
