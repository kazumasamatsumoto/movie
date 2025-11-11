# #266 「truthyな値」

四国めたん「truthyな値について学びましょう!」
ずんだもん「JavaScriptでは、trueじゃなくてもtrueとして扱われる値があるんだね!」
四国めたん「はい。数値の1、空でない文字列、配列、オブジェクトなどがtruthyです。」
ずんだもん「0や空文字列はfalseだけど、'0'という文字列はtrueになるの?」
四国めたん「その通りです。文字列が入っていればtruthyと判定されます。」
ずんだもん「空の配列[]や空のオブジェクト{}もtruthyなのは意外だね!」
四国めたん「条件分岐で値の存在チェックをする時によく使われるので覚えておきましょう。」
ずんだもん「Boolean()関数を使えば、どんな値もtrueかfalseに変換できるのだ!」

---


```typescript
/** Example 1: 基本的なtruthyな値 */
console.log(Boolean(1));         // true
console.log(Boolean('hello'));   // true
console.log(Boolean('0'));       // true (文字列の'0')

/** Example 2: オブジェクトと配列 */
console.log(Boolean([]));        // true (空配列)
console.log(Boolean({}));        // true (空オブジェクト)

/** Example 3: 関数とDate */
console.log(Boolean(function(){})); // true
console.log(Boolean(new Date())); // true
```
