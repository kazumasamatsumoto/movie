# #481 「使用例」

四国めたん「neverはバリデーションやエラーハンドラで大活躍します。」
ずんだもん「validatePositiveが条件違反でthrowしていたね。」
四国めたん「assertDefinedのようにassertsと組み合わせれば型も絞れます。」
ずんだもん「handleErrorではprocess.exit(1)で終了してた!」
四国めたん「戻らない処理をひとまとめにして再利用しやすくなります。」
ずんだもん「実際のユースケースを意識してneverを設計するのだ!"

---

## 📺 画面表示用コード

```typescript
/** Example 1: バリデーション */
function validatePositive(value: number): void {
  if (value <= 0) {
    throwError("Value must be positive");
  }
}

function throwError(message: string): never {
  throw new Error(message);
}

/** Example 2: アサーション */
function assertDefined<T>(value: T | undefined): asserts value is T {
  if (value === undefined) {
    throw new Error("Value is undefined");
  }
}

/** Example 3: エラーハンドラ */
function handleError(error: unknown): never {
  console.error("Fatal error:", error);
  process.exit(1);
}
```
