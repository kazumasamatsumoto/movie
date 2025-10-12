# #622 「未知データのバリデーション」

四国めたん「unknownを扱うならバリデーションは不可欠です」
ずんだもん「型ガード、スキーマ、assert関数を組み合わせるんだね」
四国めたん「はい。失敗時のエラー整備も重要です」
ずんだもん「共通バリデーション層を作れば再利用が効くよ」
四国めたん「バリデーションがあるほどanyからの脱却が進みます」
ずんだもん「安全な境界を作って安心して開発しよう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 型ガード */
const isUser = (value: unknown): value is { id: number } =>
  typeof value === "object" && value !== null && "id" in value;

/** Example 2: assert関数 */
function assertUser(value: unknown): asserts value is { id: number } {
  if (!isUser(value)) throw new TypeError("User expected");
}

/** Example 3: バリデーション層 */
function parseUser(json: string) {
  const data: unknown = JSON.parse(json);
  assertUser(data);
  return data;
}
```
