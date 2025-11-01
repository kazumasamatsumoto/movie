# #606 「unknown型を使うべき場面」

四国めたん「unknown型は外部境界や未確定データで積極的に使います」
ずんだもん「APIレスポンス、ユーザー入力、try-catchのerrorとかだね」
四国めたん「はい。未知の値を受け止めたあと型ガードで安全を確保します」
ずんだもん「anyの代わりに使うとコンパイルが守ってくれるよ」
四国めたん「ドメインに入る前のバリデーションステップでunknownが活躍します」
ずんだもん「境界管理の基本として採用しておこう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: API境界 */
async function fetchData(): Promise<unknown> {
  const res = await fetch("/api/data");
  return res.json();
}

/** Example 2: フォーム入力 */
function handleInput(value: unknown) {
  if (typeof value === "string") return value.trim();
  return null;
}

/** Example 3: エラーハンドリング */
try {
  throw new Error("oops");
} catch (error: unknown) {
  if (error instanceof Error) console.error(error.stack);
}
```
