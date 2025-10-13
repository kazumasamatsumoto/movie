# #900 「APIレスポンス」

四国めたん「APIレスポンスでBigIntを返すときは文字列化が必須です。」
ずんだもん「OpenAPIでもstringフォーマットを定義しておくと分かりやすいね。」
四国めたん「はい、クライアント側でBigIntへ復元する関数もセットにしましょう。」
ずんだもん「GraphQLではカスタムスカラーを定義すると直感的だよ。」
四国めたん「RESTでもJSON Schemaでpatternやformatを指定できます。」
ずんだもん「APIレスポンス設計でBigIntの精度を守ろう！」
四国めたん「契約に沿ったシリアライズとデシリアライズを徹底してください。」
ずんだもん「クライアントとサーバーで同じ規約を共有してね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: OpenAPIスキーマ */
const BalanceSchema = {
  type: "object",
  properties: {
    amount: { type: "string", pattern: "^-?\\d+$" },
  },
};

/** Example 2: GraphQLスカラー */
// scalar BigInt
// resolve: (value) => value.toString()

/** Example 3: クライアント側復元 */
function parseBalance(json: { amount: string }) {
  return { amount: BigInt(json.amount) };
}
```
