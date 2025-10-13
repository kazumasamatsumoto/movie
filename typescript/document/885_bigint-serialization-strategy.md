# #885 「シリアライズ戦略」

四国めたん「BigIntをシリアライズする戦略を整理しましょう。」
ずんだもん「送信時に文字列化、受信時にBigIntへ復元、という流れが基本だね。」
四国めたん「はい、プロトコルごとにフォーマットを決めてスキーマ化します。」
ずんだもん「GraphQLならString、gRPCならstringフィールドが妥当だよ。」
四国めたん「バイナリ形式では固定長バッファを使用しましょう。」
ずんだもん「戦略を決めてユーティリティを共通化しよう！」
四国めたん「テストとドキュメントもセットで整備すると安心です。」
ずんだもん「シリアライズ戦略をチームで共有してね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 共通ユーティリティ */
export const BigIntJSON = {
  serialize: (value: bigint) => value.toString(),
  deserialize: (value: string) => BigInt(value),
};

/** Example 2: GraphQLリゾルバ */
const resolvers = {
  Query: {
    balance: () => BigIntJSON.serialize(123456789n),
  },
};

/** Example 3: gRPCメッセージ */
interface BalanceMessage {
  amount: string;
}
function encodeBalance(value: bigint): BalanceMessage {
  return { amount: BigIntJSON.serialize(value) };
}
```
