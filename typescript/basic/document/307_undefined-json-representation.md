# #307 「undefinedのJSON表現」

四国めたん「undefinedのJSON表現について学びましょう!」
ずんだもん「JSONでundefinedはプロパティごと省略されるんだね!」
四国めたん「はい。null は '{"value":null}' として残りますが、undefinedは消えます。」
ずんだもん「配列の中のundefinedは特別で、nullに変換されるんだよね?」
四国めたん「その通りです。配列では位置を保つためnullとして扱われます。」
ずんだもん「オプショナルプロパティが省略された場合も、JSONには含まれないね!」
四国めたん「JSON.stringifyの動作を理解すると、データ送信時のトラブルを防げます。」
ずんだもん「undefinedとnullの違いがJSON変換で明確になるのだ!」

---


```typescript
/** Example 1: undefinedのJSON表現 */
JSON.stringify({ value: undefined });
// → '{}'  (undefinedは省略)
JSON.stringify({ value: null });
// → '{"value":null}'

/** Example 2: 配列内のundefined */
JSON.stringify([1, undefined, 3]);
// → '[1,null,3]'  (配列ではnullに変換)

/** Example 3: オプショナルプロパティ */
interface User {
  name: string;
  age?: number;  // undefined可能
}
JSON.stringify({ name: "Alice" });
// → '{"name":"Alice"}'
```
