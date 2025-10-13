# #854 「明示的変換 - BigInt(number)」

四国めたん「numberをBigIntに変換するときはBigInt関数を使います。」
ずんだもん「整数以外を渡すと例外になるので注意だね。」
四国めたん「はい、Number.isIntegerで検証してから変換しましょう。」
ずんだもん「numberの配列をBigIntに変換するユーティリティを作っておくと便利だよ。」
四国めたん「型変換で精度を確保して演算に備えましょう。」
ずんだもん「BigIntへの明示的変換を習慣にしてね！」
四国めたん「桁あふれが懸念される入力は早めにBigInt化すると安全です。」
ずんだもん「正しい変換で精度を守ろう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 整数変換 */
const converted = BigInt(42);

/** Example 2: ガード */
function toBigIntSafe(value: number): bigint {
  if (!Number.isInteger(value)) {
    throw new Error("integer required");
  }
  return BigInt(value);
}

/** Example 3: 配列変換 */
const bigints = [1, 2, 3].map((v) => BigInt(v));
```
