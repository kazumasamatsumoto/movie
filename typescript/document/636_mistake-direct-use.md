# #636 「間違い① 直接unknownを使う」

四国めたん「最初の間違いはunknownをガードせず直接使ってしまうことです」
ずんだもん「value.idとか書くとコンパイルが止まるけど、ついanyに戻したくなるんだよね」
四国めたん「そうです。その誘惑に負けず適切な型ガードを書く必要があります」
ずんだもん「共通ヘルパーを用意して対策しよう」
四国めたん「直接操作は禁止、ガード後に利用というルールを浸透させましょう」
ずんだもん「この間違いを避ければunknownの恩恵を最大限受けられるね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 間違い例 */
const payload: unknown = {};
// payload.id; // ❌

/** Example 2: 正しいガード */
function hasId(value: unknown): value is { id: number } {
  return typeof value === "object" && value !== null && "id" in value;
}

/** Example 3: 利用 */
if (hasId(payload)) {
  console.log(payload.id);
}
```
