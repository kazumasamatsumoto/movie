# #258 「typeof型ガードの戻り値」

四国めたん「typeofの戻り値について学びましょう!」
ずんだもん「typeofはどんな文字列を返すの?」
四国めたん「'string'、'number'、'boolean'、'object'などを返します。」
ずんだもん「配列もobjectになるんだよね?」
四国めたん「はい。そして注意点として、nullもobjectを返します。」
ずんだもん「typeof null === 'object'って有名なバグだよね!」
四国めたん「その通りです。nullチェックには===を使いましょう。」
ずんだもん「型述語関数でisNullを作れば、明示的にチェックできるのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: typeofの戻り値 */
console.log(typeof 'hello');     // 'string'
console.log(typeof 42);          // 'number'
console.log(typeof true);        // 'boolean'
console.log(typeof {});          // 'object'
console.log(typeof []);          // 'object' (配列もobject)
console.log(typeof null);        // 'object' (注意!)
console.log(typeof undefined);   // 'undefined'
console.log(typeof function(){}); // 'function'

/** Example 2: nullの正しいチェック */
function isNull(value: unknown): value is null {
  return value === null;
}
```
