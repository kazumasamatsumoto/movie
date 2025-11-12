# #483 「try-catch」

四国めたん「never関数をtry-catchで扱う例も見ておきましょう。」
ずんだもん「riskyOperation()は必ずthrowしてた!」
四国めたん「カスタムエラーを捕捉するときはinstanceofを使います。」
ずんだもん「Error型のチェックも活用できるの?」
四国めたん「はい。catch内で絞り込みましょう。」

---

## 📺 画面表示用コード

```typescript
/** Example 1: never関数のtry-catch */
function riskyOperation(): never {
  throw new Error("Operation failed");
}
try {
  riskyOperation();
} catch (error) {
  console.error("Caught:", error);
}

/** Example 2: カスタムエラー */
class ValidationError extends Error {}
function validate(data: unknown): never {
  throw new ValidationError("Invalid");
}
try {
  validate(data);
} catch (error) {
  if (error instanceof ValidationError) {
    console.error("Validation failed");
  }
}

/** Example 3: Error型チェック */
try {
  throwError("Error");
} catch (error) {
  if (error instanceof Error) {
    console.error(error.message);
  }
}
```
