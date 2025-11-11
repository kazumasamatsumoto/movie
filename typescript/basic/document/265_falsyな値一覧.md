# #265 「falsyな値一覧」

四国めたん「falsyな値一覧について学びましょう!」
ずんだもん「全部でいくつあるの?」
四国めたん「はい。JavaScriptのfalsyな値は全部で6つだけです。」
ずんだもん「false、0、空文字、null、undefined、NaNだね!」
四国めたん「その通りです。これら以外の全ての値はtruthyになります。」
ずんだもん「注意すべき値もある?」
四国めたん「はい。'0'、[]、{}は一見falsyに見えますが、実はtruthyです。」
ずんだもん「この6つを覚えておけば完璧なのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: falsyな値一覧（全6つ） */
console.log(Boolean(false));     // false
console.log(Boolean(0));         // false
console.log(Boolean(''));        // false
console.log(Boolean(null));      // false
console.log(Boolean(undefined)); // false
console.log(Boolean(NaN));       // false

/** Example 2: 注意: これらはtruthyです */
console.log(Boolean('0'));       // true (文字列)
console.log(Boolean([]));        // true (空配列)
console.log(Boolean({}));        // true (空オブジェクト)
```
