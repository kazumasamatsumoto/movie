# #886 「デシリアライズ」

四国めたん「文字列からBigIntへ戻すデシリアライズ処理を整えましょう。」
ずんだもん「Number()で変換すると精度が落ちるから必ずBigInt()を使うんだね。」
四国めたん「はい、入力検証を行って想定外の形式を弾きます。」
ずんだもん「JSON.parseのreviverやDTOのコンストラクタで変換すると便利だよ。」
四国めたん「例外時のエラー処理も整備しましょう。」
ずんだもん「デシリアライズでBigIntの安全性を保とう！」
四国めたん「復元処理を共通化して重複を減らしてください。」
ずんだもん「受信側の責任を明確にしようね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 検証 */
function parseBigint(value: string): bigint {
  if (!/^[-+]?\d+$/.test(value)) {
    throw new Error("invalid bigint format");
  }
  return BigInt(value);
}

/** Example 2: DTO */
class BalanceDTO {
  constructor(public readonly amount: bigint) {}
  static fromJSON(json: { amount: string }) {
    return new BalanceDTO(parseBigint(json.amount));
  }
}

/** Example 3: reviver */
const revived = JSON.parse('{"amount":"42"}', (_, v) =>
  typeof v === "string" && /^\d+$/.test(v) ? BigInt(v) : v,
);
```
