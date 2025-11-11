# #305 「typeof undefined」

四国めたん「typeof undefinedについて学びましょう!」
ずんだもん「typeof演算子でundefinedを調べるとどうなる?」
四国めたん「はい。文字列"undefined"が返されます。」
ずんだもん「typeof null は"object"なのに違うんだね!」
四国めたん「その通りです。typeof演算子でチェックもできます。」
ずんだもん「typeof value === "undefined"で確認するの?」
四国めたん「はい。未宣言の変数でもエラーにならず安全です。」
ずんだもん「直接===だとReferenceErrorになるけど、typeofなら大丈夫なのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: typeof undefined */
typeof undefined; // "undefined"
typeof null;      // "object"

/** Example 2: typeof でチェック */
if (typeof value === "undefined") {
  console.log("undefined");
}

/** Example 3: 未宣言の変数も安全 */
typeof undeclaredVar === "undefined"; // true (エラーなし)
undeclaredVar === undefined; // ReferenceError
```
