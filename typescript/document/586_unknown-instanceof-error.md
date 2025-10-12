# #586 「x instanceof Error」

四国めたん「x instanceof ErrorでunknownをError型に絞れます」
ずんだもん「try-catchのerrorを安全に扱えるやつだね」
四国めたん「はい。messageやstackへアクセスする前に必ず判定しましょう」
ずんだもん「独自エラーも継承すれば同じ判定で使えるよ」
四国めたん「Error境界の安全性が劇的に向上します」
ずんだもん「ログも型安全に取れるようになるね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: try-catch */
try {
  throw new Error("fail");
} catch (error: unknown) {
  if (error instanceof Error) {
    console.error(error.message);
  }
}

/** Example 2: 独自エラー */
class HttpError extends Error {
  constructor(public status: number, message: string) {
    super(message);
  }
}
const err: unknown = new HttpError(500, "server");
if (err instanceof HttpError) console.log(err.status);

/** Example 3: ログユーティリティ */
function log(error: unknown) {
  if (error instanceof Error) console.error(error.stack);
}
```
