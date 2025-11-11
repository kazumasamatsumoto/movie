# #263 「truthyチェック」

四国めたん「truthyチェックについて学びましょう!」
ずんだもん「値が存在するかチェックする方法だね!」
四国めたん「はい。if文で値を直接評価するとtruthyかどうか判定できます。」
ずんだもん「truthyな値ってどんなもの?」
四国めたん「その通りです。0以外の数値、空でない文字列、配列、オブジェクトなどです。」
ずんだもん「Boolean関数で確認できる?」
四国めたん「はい。Boolean()を使えば、任意の値がtruthyかfalsyか確認できます。」
ずんだもん「値の存在チェックに便利なのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: truthyチェック */
function process(value: string | number | null) {
  if (value) {
    // truthyな値の場合
    console.log('値が存在します');
  }
}

/** Example 2: truthy値の例 */
console.log(Boolean(1));        // true
console.log(Boolean('hello'));  // true
console.log(Boolean([]));       // true
console.log(Boolean({}));       // true
console.log(Boolean(true));     // true
```
