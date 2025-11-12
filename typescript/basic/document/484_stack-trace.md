# #484 「スタックトレース」

四国めたん「never関数ではスタックトレースを活用しましょう。」
ずんだもん「failでerror.stackをログしていたね。」
四国めたん「カスタムエラーならcaptureStackTraceで綺麗に取れます。」
ずんだもん「try-catchでスタックを表示する例もあった!」
四国めたん「デバッグ用に情報を残すと原因が追いやすくなります。」

---

## 📺 画面表示用コード

```typescript
/** Example 1: スタック表示 */
function fail(message: string): never {
  const error = new Error(message);
  console.error(error.stack);
  throw error;
}

/** Example 2: カスタムエラー */
class AppError extends Error {
  constructor(message: string) {
    super(message);
    this.name = "AppError";
    Error.captureStackTrace(this, AppError);
  }
}
function throwAppError(): never {
  throw new AppError("Application error");
}

/** Example 3: スタックの利用 */
try {
  fail("Something went wrong");
} catch (error) {
  if (error instanceof Error) {
    console.error("Stack trace:", error.stack);
  }
}
```
