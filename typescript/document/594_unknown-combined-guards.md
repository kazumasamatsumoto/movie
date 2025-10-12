# #594 「複合型ガード」

四国めたん「複合型ガードでunknownを多段で絞り込みましょう」
ずんだもん「typeofやin演算子を組み合わせて厳密にチェックするんだよね」
四国めたん「はい。ネストしたオブジェクトでも安全に扱えます」
ずんだもん「再利用可能なヘルパーにすればテストも書きやすいよ」
四国めたん「複合ガードがあればドメインロジックが強固になります」
ずんだもん「未知のデータを確実に期待型へ導けるね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 複合ガード */
type User = { id: number; profile: { name: string } };
function isUser(value: unknown): value is User {
  return typeof value === "object" && value !== null
    && "id" in value && typeof (value as Record<string, unknown>).id === "number"
    && "profile" in value && typeof (value as Record<string, unknown>).profile === "object";
}

/** Example 2: ネストチェック */
const hasName = (value: unknown): value is { profile: { name: string } } =>
  typeof value === "object" && value !== null
  && "profile" in value
  && typeof (value as Record<string, unknown>).profile === "object"
  && (value as { profile: Record<string, unknown> }).profile !== null
  && "name" in (value as { profile: Record<string, unknown> }).profile;

/** Example 3: 利用例 */
const payload: unknown = { id: 1, profile: { name: "Zen" } };
if (isUser(payload) && hasName(payload)) console.log(payload.profile.name);
```
