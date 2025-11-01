# #722 「代替実例①」

四国めたん「実例としてAPIレスポンスのanyをUnionで置き換えたケースを紹介します」
ずんだもん「successとerrorの判別ユニオンを作ったんだよね」
四国めたん「はい。フロント側の分岐ロジックが安全になり補完も向上しました」
ずんだもん「テストでは各パターンを明示的にチェックできるようになったよ」
四国めたん「Union型がanyの代わりに契約を明確化した良い例です」
ずんだもん「実装とテストをセットで整えよう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 判別ユニオン */
type ApiResponse =
  | { status: "success"; data: { id: string } }
  | { status: "error"; message: string };

/** Example 2: anyからの置換 */
async function fetchUser(): Promise<ApiResponse> {
  const res = await fetch("/api/user");
  if (!res.ok) return { status: "error", message: "failed" };
  return { status: "success", data: await res.json() };
}

/** Example 3: 利用 */
const result = await fetchUser();
if (result.status === "success") console.log(result.data.id);
else console.error(result.message);
```
