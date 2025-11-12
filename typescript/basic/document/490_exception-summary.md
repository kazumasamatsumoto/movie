# #490 「例外まとめ」

四国めたん「neverと例外処理のまとめです。」
ずんだもん「fail(message)のような例外関数が基本!」
四国めたん「assertNeverで網羅性チェックも忘れずに。」
ずんだもん「カスタムエラーをtry-catchする例もありました。」
四国めたん「neverを使った例外設計を総復習しましょう。」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 例外を投げる関数 */
function fail(message: string): never {
  throw new Error(message);
}

/** Example 2: 網羅性チェック */
function assertNever(value: never): never {
  throw new Error(`Unhandled: ${value}`);
}

/** Example 3: カスタムエラーとtry-catch */
class AppError extends Error {}
try {
  throw new AppError("Error");
} catch (error) {
  if (error instanceof AppError) {
    console.error(error.message);
  }
}
```
