# #489 「ベストプラクティス」

四国めたん「neverのベストプラクティスを押さえましょう。」
ずんだもん「throwErrorやassertNeverのように明示的な関数を用意するんだね。」
四国めたん「カスタムエラーで詳細を伝えるのも重要です。」
ずんだもん「網羅性チェックも忘れちゃいけない!」
四国めたん「これらを揃えるとエラー設計が整います。」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 明示的な関数 */
function throwError(message: string): never {
  throw new Error(message);
}
function assertNever(value: never): never {
  throw new Error(`Unexpected: ${value}`);
}

/** Example 2: 詳細なエラー */
class ValidationError extends Error {
  constructor(public field: string, message: string) {
    super(`${field}: ${message}`);
  }
}
function validate(field: string, value: unknown): never {
  throw new ValidationError(field, "Invalid value");
}

/** Example 3: 網羅性チェック */
type Status = "idle" | "loading" | "success" | "error";
function handleStatus(status: Status): void {
  switch (status) {
    case "idle":
    case "loading":
    case "success":
    case "error":
      return;
    default:
      assertNever(status);
  }
}
```
