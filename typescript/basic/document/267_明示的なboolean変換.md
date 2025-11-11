# #267 「明示的なboolean変換」

四国めたん「明示的なboolean変換について学びましょう!」
ずんだもん「Boolean()関数を使うと、値を明確にtrueかfalseに変換できるんだね!」
四国めたん「はい。もう一つの方法として!!演算子(二重否定)もよく使われます。」
ずんだもん「!!演算子は!を2回使うから、falseをtrueに、trueをfalseに、さらにもう一度反転するの?」
四国めたん「その通りです。結果的に元の値のboolean表現が得られます。」
ずんだもん「型安全な関数を作る時はBoolean()を使うほうが読みやすいね!」
四国めたん「条件式でユーザー入力を検証する時などに特に有用です。」
ずんだもん「暗黙的な変換より明示的な変換のほうがコードの意図が伝わりやすいのだ!」

---


```typescript
/** Example 1: Boolean()関数 */
const value1 = Boolean('hello'); // true
const value2 = Boolean(0);       // false

/** Example 2: !!演算子(二重否定) */
const value3 = !!'hello';  // true
const value4 = !!0;        // false

/** Example 3: 型安全な変換関数 */
function toBoolean(value: unknown): boolean {
  return Boolean(value);
}
```
