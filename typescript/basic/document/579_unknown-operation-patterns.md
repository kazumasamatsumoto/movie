# #579 「unknown操作パターン」

四国めたん「unknownを操作するパターンを分類しましょう」
ずんだもん「判定、変換、委譲の三つに分けられるよね」
四国めたん「はい。判定で絞り、変換で具体化し、必要なら別関数へ委譲します」
ずんだもん「パターンごとにヘルパーを作ると実装が楽だよ」
四国めたん「粒度を揃えておけばレビューもしやすくなります」
ずんだもん「パターン設計でunknownの扱いが洗練されるね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 判定パターン */
const isBoolean = (value: unknown): value is boolean =>
  typeof value === "boolean";

/** Example 2: 変換パターン */
function toNumber(value: unknown): number | null {
  if (typeof value === "number") return value;
  if (typeof value === "string") return Number(value);
  return null;
}

/** Example 3: 委譲パターン */
function handle(value: unknown, delegate: (v: string) => void) {
  if (typeof value === "string") delegate(value);
}
```
