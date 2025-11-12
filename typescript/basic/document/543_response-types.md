# #543 「レスポンス型」

四国めたん「レスポンス型でもneverで状態漏れを防ごう。」
ずんだもん「ApiResponse<T>はsuccess/error/loadingの3状態でhandleResponse()が全部処理してた。」
四国めたん「PagedResponse<T>はhasDataフラグでデータ有無を表してたね。」
ずんだもん「reasonがemptyかerrorのどちらかで、最後にcheck: never = res; を置くのだ。」
四国めたん「HttpResponse<T>ではHTTPステータスごとに返り値を分けてた。」
ずんだもん「status>=400の場合だけエラーを投げて、それ以外はデータやnullを返してたよ。」
四国めたん「レスポンス型を固めるとAPIクライアントの実装も安全になる。」
ずんだもん「どのケースもneverが監視してくれるね。」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 標準レスポンス */
type ApiResponse<T> =
  | { status: "success"; data: T; timestamp: number }
  | { status: "error"; error: { code: string; message: string } }
  | { status: "loading" };

function handleResponse<T>(res: ApiResponse<T>): T | null {
  if (res.status === "success") return res.data;
  if (res.status === "error") {
    console.error(res.error);
    return null;
  }
  if (res.status === "loading") return null;
  const check: never = res;
  return null;
}
```

```typescript
/** Example 2: ページネーション */
type PagedResponse<T> =
  | { hasData: true; items: T[]; total: number; page: number }
  | { hasData: false; reason: "empty" | "error" };

function processPage<T>(res: PagedResponse<T>): T[] {
  if (res.hasData) return res.items;
  if (!res.hasData && res.reason === "empty") return [];
  if (!res.hasData && res.reason === "error") throw new Error("Failed");
  const check: never = res;
  return [];
}
```

```typescript
/** Example 3: HTTPレスポンス */
type HttpResponse<T> =
  | { status: 200; data: T }
  | { status: 201; data: T; location: string }
  | { status: 204 }
  | { status: 400 | 404 | 500; error: string };

function handle<T>(res: HttpResponse<T>): T | null {
  if (res.status === 200) return res.data;
  if (res.status === 201) return res.data;
  if (res.status === 204) return null;
  if (res.status >= 400) throw new Error(res.error);
  const check: never = res;
  return null;
}
```
