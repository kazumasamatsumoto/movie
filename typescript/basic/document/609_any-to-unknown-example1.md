# #609 「anyからunknown移行・実例1」

四国めたん「実例としてユーザーAPIのanyをunknownへ移行しましょう」
ずんだもん「まずfetchUserの戻り値をunknownに変えるんだね」
四国めたん「はい。その後型ガードでUser型に絞ってDTOへ変換します」
ずんだもん「テストで安全性を確認できる構造になるよ」
四国めたん「既存コードも小さく改修して安全にできます」
ずんだもん「実務で試してunknownの効果を体感しよう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 変更前 */
async function fetchUserLegacy(): Promise<any> {
  const res = await fetch("/api/user");
  return res.json();
}

/** Example 2: 変更後 */
type User = { id: number; name: string };
async function fetchUser(): Promise<unknown> {
  const res = await fetch("/api/user");
  return res.json();
}

/** Example 3: 型ガードで利用 */
function toUser(value: unknown): User | null {
  if (typeof value === "object" && value !== null && "id" in value && "name" in value) {
    const record = value as Record<string, unknown>;
    if (typeof record.id === "number" && typeof record.name === "string") {
      return { id: record.id, name: record.name };
    }
  }
  return null;
}
```
