# #476 「throw文を含む関数」

四国めたん「throw文を含む関数はneverで型付けしましょう。」
ずんだもん「fail(message)のようにいつでも例外を投げるんだね。」
四国めたん「assert(condition)も失敗時はneverとみなせます。」
ずんだもん「divide関数でゼロ除算時にthrowErrorを呼んでいた!」
四国めたん「エラー設計を型で表現すると利用者が助かります。」

---

## 📺 画面表示用コード

```typescript
/** Example 1: throwError */
function throwError(message: string): never {
  throw new Error(message);
}

/** Example 2: アサート関数 */
function assert(condition: boolean, message: string): asserts condition {
  if (!condition) {
    throw new Error(message);
  }
}

/** Example 3: 使用例 */
function divide(a: number, b: number): number {
  if (b === 0) {
    throwError("Division by zero");
  }
  return a / b;
}
```
