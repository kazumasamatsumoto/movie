# #618 「APIレスポンスの型安全化」

四国めたん「APIレスポンスはunknownで受けて型安全に変換しましょう」
ずんだもん「サーバーから何が来るかわからないからね」
四国めたん「はい。型ガードやスキーマ検証でDTOにマップします」
ずんだもん「レスポンスがエラーでもハンドリングしやすくなるよ」
四国めたん「共通パイプラインを用意するとチーム全体で恩恵があります」
ずんだもん「API層でunknown→具体型の流れを徹底しよう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: API呼び出し */
async function fetchPost(): Promise<unknown> {
  const res = await fetch("/api/post");
  return res.json();
}

/** Example 2: DTO変換 */
type Post = { id: number; title: string };
const isPost = (value: unknown): value is Post =>
  typeof value === "object" && value !== null
  && typeof (value as Record<string, unknown>).id === "number"
  && typeof (value as Record<string, unknown>).title === "string";

/** Example 3: パイプライン */
async function loadPost() {
  const payload = await fetchPost();
  if (!isPost(payload)) throw new TypeError("invalid post");
  return payload;
}
```
