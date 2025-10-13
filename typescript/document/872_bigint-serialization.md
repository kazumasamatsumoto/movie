# #872 「シリアライズ」

四国めたん「BigIntをシリアライズするときは文字列か専用フォーマットを使います。」
ずんだもん「JSONなら文字列、バイナリなら固定長バイト列が定番だね。」
四国めたん「はい、toStringで基数を決めたり、Bufferに変換したりします。」
ずんだもん「シリアライズ時に符号や桁数も一緒に持たせると復元が楽だよ。」
四国めたん「プロトコルを統一しておくと後方互換が保てます。」
ずんだもん「シリアライズ戦略を設計してBigIntを安全に運搬しよう！」
四国めたん「復元側のエラーハンドリングも忘れずに。」
ずんだもん「BigIntを信頼して渡すにはフォーマットが命だよ！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: JSON文字列 */
function serializeBigint(value: bigint) {
  return { value: value.toString() };
}

/** Example 2: Buffer変換 */
function toBuffer(value: bigint): Buffer {
  let hex = value.toString(16);
  if (hex.length % 2) hex = "0" + hex;
  return Buffer.from(hex, "hex");
}

/** Example 3: 復元 */
function parseBigint(payload: { value: string }): bigint {
  return BigInt(payload.value);
}
```
