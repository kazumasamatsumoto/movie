# #596 「型述語で安全宣言」

四国めたん「型述語は関数の戻り値で型を保証する仕組みです」
ずんだもん「value is Type って書くと呼び出し元で型が絞り込まれるんだよね」
四国めたん「はい。unknownの安全な取り扱いに欠かせません」
ずんだもん「テスト可能なロジックとして切り出せるのも魅力だよ」
四国めたん「型述語を活用して証明責任を関数に委譲しましょう」
ずんだもん「ガード関数をどんどん資産化していこう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 型述語の定義 */
function isUser(value: unknown): value is { id: number } {
  return typeof value === "object"
    && value !== null
    && "id" in value
    && typeof (value as Record<string, unknown>).id === "number";
}

/** Example 2: 呼び出し側の推論 */
const payload: unknown = { id: 1 };
if (isUser(payload)) {
  console.log(payload.id);
}

/** Example 3: テスト例 */
console.assert(isUser({ id: 1 }) === true);
console.assert(isUser({}) === false);
```
