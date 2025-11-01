# #891 「暗号化」

四国めたん「BigIntは公開鍵暗号などの整数演算に欠かせません。」
ずんだもん「RSAのモジュラー指数演算なんかが代表例だね。」
四国めたん「TypeScriptでもmodPowを実装すれば暗号処理を表現できます。」
ずんだもん「ライブラリを使う場合もBigInt型を扱えるか確認しよう。」
四国めたん「キーサイズが大きいほどBigIntの恩恵が増します。」
ずんだもん「暗号計算を安全に行うためにBigIntを活用しよう！」
四国めたん「想定外の丸めを防ぎ、正確な演算が可能です。」
ずんだもん「セキュリティ領域でBigIntが活躍するよ！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: モジュラー指数 */
function modPow(base: bigint, exponent: bigint, modulus: bigint): bigint {
  if (modulus === 1n) return 0n;
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

/** Example 2: RSA演算サンプル */
const n = 3233n; // 小さなRSAモジュラス
const e = 17n;
const message = 65n;
const encrypted = modPow(message, e, n);

/** Example 3: 復号 */
const d = 2753n;
const decrypted = modPow(encrypted, d, n);
```
