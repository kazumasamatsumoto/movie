# #251 「文字列の比較」

四国めたん「文字列の比較について学びましょう!」
ずんだもん「文字列も比較演算子で比較できるの?」
四国めたん「はい。文字列は辞書順（Unicode順）で比較されます。」
ずんだもん「'apple' < 'banana'はtrueになるんだね!」
四国めたん「その通りです。大文字と小文字では、大文字の方が小さいと判定されます。」
ずんだもん「'A' < 'a'もtrueになるの?」
四国めたん「はい。長さの異なる文字列も比較でき、'abc' < 'abcd'はtrueです。」
ずんだもん「型安全な文字列比較関数を作ると、もっと便利になるのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 辞書順の比較 */
console.log('apple' < 'banana'); // true
console.log('cat' > 'dog');      // false

/** Example 2: 大文字と小文字 */
console.log('A' < 'a');  // true
console.log('Z' < 'a');  // true

/** Example 3: 型安全な文字列比較 */
function compareStrings(a: string, b: string): number {
  return a === b ? 0 : a < b ? -1 : 1;
}
```
