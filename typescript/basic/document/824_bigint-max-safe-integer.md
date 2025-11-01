# #824 「MAX_SAFE_INTEGER」

四国めたん「JavaScriptのnumberで安全に表現できる最大整数はNumber.MAX_SAFE_INTEGERです。」
ずんだもん「9,007,199,254,740,991だね。」
四国めたん「これを超えると整数演算が破綻します。」
ずんだもん「BigIntならこの制限を超えても正確だよ。」
四国めたん「超えるかどうかをチェックしてBigIntへ切り替えましょう。」
ずんだもん「限界値を知ると設計の指針になるね。」
四国めたん「MAX_SAFE_INTEGERはBigInt移行の目安です。」
ずんだもん「境界値を意識して精度を守ろう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 安全な最大値 */
console.log(Number.MAX_SAFE_INTEGER); // 9007199254740991

/** Example 2: 超えた場合 */
const unsafe = Number.MAX_SAFE_INTEGER + 1;
console.log(unsafe === unsafe + 1); // true

/** Example 3: BigIntで回避 */
const safeBig = BigInt(Number.MAX_SAFE_INTEGER) + 1n;
console.log(safeBig === safeBig + 1n); // false
```
