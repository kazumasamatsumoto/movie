# #947 「Union型の配列宣言」

四国めたん「混合型配列はUnion型を括弧で囲んで宣言します。」
ずんだもん「(string | number)[]みたいにね。」
四国めたん「はい、Array<string | number>でも同じ意味です。」
ずんだもん「Union部分を括弧で囲まないとnumber[] | string[]になっちゃうから気をつけよう。」
四国めたん「宣言時に意図した型を明確にしましょう。」
ずんだもん「Union型配列の書き方を覚えてね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 括弧付き */
const values: (string | number)[] = ["ok", 200];

/** Example 2: Array<T> */
const responses: Array<string | number> = ["timeout", 504];

/** Example 3: 括弧なしの落とし穴 */
// const wrong: string[] | number[] = ["ok", 200]; // エラー
```
