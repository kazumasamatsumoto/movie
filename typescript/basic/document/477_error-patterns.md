# #477 「型安全なエラーパターン」

四国めたん「neverは型安全なエラー処理にも役立ちます。」
ずんだもん「exhaustiveCheckで漏れを型エラーにできたね。」
四国めたん「assertNever(value)と同じ発想で失敗を明示します。」
ずんだもん「neverで例外設計を体系化するのだ!"

---

## 📺 画面表示用コード

```typescript
/** Example 1: exhaustiveCheck */
function exhaustiveCheck(value: never): never {
  throw new Error(`Unhandled case: ${value}`);
}

/** Example 2: assertNever */
function assertNever(value: never): never {
  throw new Error(`Unexpected value: ${value}`);
}

/** Example 3: 使用例 */
type Status = "pending" | "success";
function handleStatus(status: Status): void {
  switch (status) {
    case "pending": return;
    case "success": return;
    default: assertNever(status);
  }
}
```
