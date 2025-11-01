# #577 「unknownの安全な扱い方」

四国めたん「unknownを安全に扱うには手順を決めましょう」
ずんだもん「受け取る→検証→変換→利用というフローだね」
四国めたん「ログや失敗時のフォールバックも用意しておくと安心です」
ずんだもん「ヘルパーで共通化すればミスも減るよ」
四国めたん「安全な扱い方をチームドキュメントに落とし込みましょう」
ずんだもん「実践で擦り合わせるのが大事だね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 基本フロー */
function safeUse(input: unknown) {
  if (typeof input === "string") return input.trim();
  return String(input);
}

/** Example 2: ログとフォールバック */
function handle(input: unknown) {
  if (typeof input !== "number") {
    console.warn("unexpected", input);
    return 0;
  }
  return input;
}

/** Example 3: ヘルパーの再利用 */
const isArrayOfStrings = (value: unknown): value is string[] =>
  Array.isArray(value) && value.every((item) => typeof item === "string");
```
