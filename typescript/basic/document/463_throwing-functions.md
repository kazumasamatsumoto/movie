# #463 「例外を投げる関数」

四国めたん「例外を投げる関数はneverで表現します。」
ずんだもん「throwError(message) のように書くんだね。」
四国めたん「assert関数も失敗時はneverになります。」
ずんだもん「divide関数でゼロ除算を検知したらthrowErrorしてた!」
四国めたん「戻らないことを型で保証すると利用側が楽になります。」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 例外を投げる */
function throwError(message: string): never {
  throw new Error(message);
}

/** Example 2: アサーション関数 */
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
