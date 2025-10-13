# #857 「大きな数値の計算例」

四国めたん「大きな数をBigIntで計算する例を紹介します。」
ずんだもん「階乗とか累積の積を扱うのが分かりやすいね。」
四国めたん「はい、50!や桁数の大きいフィボナッチを計算してみましょう。」
ずんだもん「numberではInfinityになってしまう値もBigIntなら保持できるよ。」
四国めたん「結果を文字列に変換して扱うのがポイントです。」
ずんだもん「大きな計算をBigIntで安全に試してみよう！」
四国めたん「計算時間に注意しながら活用してください。」
ずんだもん「大規模整数の実力を感じてね！」

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
const fact50 = factorial(50n);

/** Example 2: フィボナッチ */
function fib(n: bigint): bigint {
  let a = 0n, b = 1n;
  for (let i = 0n; i < n; i++) {
    [a, b] = [b, a + b];
  }
  return a;
}

/** Example 3: 桁数表示 */
console.log(fact50.toString().length);
```
