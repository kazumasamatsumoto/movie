# #486 「エラー関数設計」

四国めたん「エラー関数は名前やコンテキストを工夫しましょう。」
ずんだもん「throwValidationError(field, reason) で分かりやすくしてた!」
四国めたん「assertPositiveのように呼び出し側へ情報を渡すと親切です。」
ずんだもん「createError(type, message) で再利用性も上がるんだね。」
四国めたん「設計されたnever関数は保守性を高めます。」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 明確なエラー名 */
function throwValidationError(field: string, reason: string): never {
  throw new Error(`Validation failed for ${field}: ${reason}`);
}

/** Example 2: コンテキストを含む */
function assertPositive(value: number, name: string): void {
  if (value <= 0) {
    throwError(`${name} must be positive, got ${value}`);
  }
}
function throwError(message: string): never {
  throw new Error(message);
}

/** Example 3: 再利用可能 */
function createError(type: string, message: string): never {
  throw new Error(`[${type}] ${message}`);
}
function validateUser(user: unknown): void {
  if (!user) {
    createError("VALIDATION", "User is required");
  }
}
```
