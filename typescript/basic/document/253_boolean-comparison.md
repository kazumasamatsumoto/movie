# #253 「booleanの比較」

四国めたん「booleanの比較について学びましょう!」
ずんだもん「true同士、false同士を比較するんだね!」
四国めたん「はい。厳密等価演算子===を使うのが基本です。」
ずんだもん「true === trueはtrueで、true === falseはfalseだね!」
四国めたん「その通りです。==と===では結果が異なる場合があります。」
ずんだもん「true == 1はtrueになるの?」
四国めたん「はい。==は型変換を行いますが、===は型まで厳密に比較します。」
ずんだもん「型安全な比較関数を作って、明示的に扱うのが大事なのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 厳密な比較 */
console.log(true === true);   // true
console.log(false === false); // true
console.log(true === false);  // false

/** Example 2: 型の違い */
console.log(true === 1);  // false
console.log(true == 1);   // true

/** Example 3: 型安全な比較関数 */
function isSameBoolean(a: boolean, b: boolean): boolean {
  return a === b;
}
```
