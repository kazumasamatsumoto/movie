# #474 「ユースケース」

四国めたん「neverの主要用途は網羅性チェックとエラー処理です。」
ずんだもん「exhaustiveCheck(value: never) が便利そう!」
四国めたん「switchやunionで漏れがあるとコンパイルエラーになります。」
ずんだもん「assertNonNullも失敗時にnever扱いになるんだね。」
四国めたん「ランタイム検証と型安全性を両方確保できます。」
ずんだもん「実務に役立つneverパターンを覚えるのだ!"

---

## 📺 画面表示用コード

```typescript
/** Example 1: 網羅性チェック */
function exhaustiveCheck(value: never): never {
  throw new Error(`Unhandled case: ${value}`);
}
type Status = "pending" | "success" | "error";
function handleStatus(status: Status): void {
  switch (status) {
    case "pending": return;
    case "success": return;
    case "error": return;
    default: exhaustiveCheck(status);
  }
}

/** Example 2: エラー処理 */
function assertNonNull<T>(value: T | null): asserts value is T {
  if (value === null) {
    throw new Error("Value is null");
  }
}

/** Example 3: 到達不可の検知 */
function unreachable(value: never): never {
  throw new Error(`Unexpected: ${value}`);
}
```
