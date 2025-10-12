# #627 「any/unknownとエラーハンドリング」

四国めたん「エラーハンドリングでもunknownは活躍します」
ずんだもん「try-catchのerrorはunknownで受けるんだよね」
四国めたん「はい。instanceofやカスタムガードで型を確定してから処理します」
ずんだもん「anyのままだとログ出力で落ちる可能性があるよ」
四国めたん「専用のエラーラッパーを用意すると保守しやすくなります」
ずんだもん「安全なエラーハンドリングで障害を未然に防ごう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: try-catch */
try {
  risky();
} catch (error: unknown) {
  if (error instanceof Error) console.error(error.message);
}

/** Example 2: カスタム判定 */
interface ApiError { code: string; message: string }
const isApiError = (value: unknown): value is ApiError =>
  typeof value === "object" && value !== null && "code" in value;

/** Example 3: ラッパー */
function handleError(error: unknown) {
  if (isApiError(error)) return error.code;
  if (error instanceof Error) return error.message;
  return "unknown";
}
```
