# #261 「Array.isArray()」

四国めたん「Array.isArray()について学びましょう!」
ずんだもん「配列かどうかを判定するメソッドなんだね!」
四国めたん「はい。typeofでは配列もobjectになってしまうので、このメソッドが必要です。」
ずんだもん「string[] | stringのような型で使えるの?」
四国めたん「その通りです。配列ならjoin()、文字列ならtoUpperCase()が使えます。」
ずんだもん「nullや空オブジェクトもちゃんとfalseになる?」
四国めたん「はい。配列のみtrueを返すので、正確な判定ができます。」
ずんだもん「配列専用の処理を安全に書けるから便利なのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 基本的な使用例 */
function processValue(value: string[] | string) {
  if (Array.isArray(value)) {
    console.log(value.join(', '));
  } else {
    console.log(value.toUpperCase());
  }
}

/** Example 2: 配列かどうかの判定 */
console.log(Array.isArray([]));       // true
console.log(Array.isArray([1, 2]));   // true
console.log(Array.isArray('hello')); // false
console.log(Array.isArray({}));       // false
console.log(Array.isArray(null));     // false
```
