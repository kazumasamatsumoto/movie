# #617 「JSON.parse()を型安全に使う」

四国めたん「JSON.parse()を型安全に使うには検証ステップを追加します」
ずんだもん「parse→unknown→型ガードって流れだね」
四国めたん「はい。スキーマバリデーションを使うのも強力です」
ずんだもん「失敗時は例外を投げるかフォールバックを返すようにしよう」
四国めたん「ラッパーを共通化すれば全体で安全に扱えます」
ずんだもん「JSONとの橋渡しを型安全に整備しよう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: セーフラッパー */
function parseSafe<T>(text: string, guard: (value: unknown) => value is T): T {
  const parsed: unknown = JSON.parse(text);
  if (!guard(parsed)) throw new TypeError("invalid JSON");
  return parsed;
}

/** Example 2: ガード関数 */
const isUser = (value: unknown): value is { id: number } =>
  typeof value === "object" && value !== null && "id" in value;

/** Example 3: 利用例 */
const user = parseSafe('{ "id": 1 }', isUser);
console.log(user.id);
```
