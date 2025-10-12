# #603 「unknown型の安全性」

四国めたん「unknown型はanyの柔軟性を保ちつつ安全性を確保します」
ずんだもん「直接操作できないから型ガードが必須なんだよね」
四国めたん「はい。静的チェックが危険な操作を止めてくれます」
ずんだもん「型推論も壊れないから保守性が高いよ」
四国めたん「unknownを基準にすると型安全なコードベースが作れます」
ずんだもん「柔軟だけど安全、これがunknownの魅力だね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 操作を制限 */
const data: unknown = "text";
// data.trim(); // ❌
if (typeof data === "string") data.trim();

/** Example 2: 型推論を保持 */
function wrap(value: unknown) {
  if (typeof value === "number") return value.toFixed(2);
  return String(value);
}

/** Example 3: 安全なエラーハンドリング */
try {
  throw new Error("fail");
} catch (error: unknown) {
  if (error instanceof Error) console.error(error.message);
}
```
