# #896 「大きな素数」

四国めたん「大きな素数の生成やチェックにもBigIntが必要です。」
ずんだもん「ミラー–ラビン素数判定みたいな確率的アルゴリズムが使えるよね。」
四国めたん「BigIntでmodPowを使ったテストが可能です。」
ずんだもん「暗号キー生成や数学シミュレーションで役立つよ。」
四国めたん「TypeScriptでも軽量な素数判定を実装してみましょう。」
ずんだもん「大きな素数を扱うときはBigIntが不可欠だね。」
四国めたん「性能と精度のバランスを見ながら活用してください。」
ずんだもん「巨大素数の世界に挑戦しよう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: モジュラー指数 */
function modPow(base: bigint, exponent: bigint, modulus: bigint): bigint {
  let result = 1n;
  let b = base % modulus;
  let e = exponent;
  while (e > 0n) {
    if (e & 1n) result = (result * b) % modulus;
    e >>= 1n;
    b = (b * b) % modulus;
  }
  return result;
}

/** Example 2: ミラー–ラビンテスト */
function isProbablePrime(n: bigint, k = 5): boolean {
  if (n < 2n || n % 2n === 0n) return n === 2n;
  let d = n - 1n;
  let r = 0n;
  while (d % 2n === 0n) {
    d /= 2n;
    r++;
  }
  const bases = [2n, 3n, 5n, 7n, 11n].slice(0, k);
  for (const a of bases) {
    if (a >= n - 2n) continue;
    let x = modPow(a, d, n);
    if (x === 1n || x === n - 1n) continue;
    let passed = false;
    for (let i = 1n; i < r; i++) {
      x = (x * x) % n;
      if (x === n - 1n) {
        passed = true;
        break;
      }
    }
    if (!passed) return false;
  }
  return true;
}

/** Example 3: 使用 */
console.log(isProbablePrime(2n ** 61n - 1n));
```
