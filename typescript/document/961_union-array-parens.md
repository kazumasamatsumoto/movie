# #961 「(string | number)[]」

四国めたん「(string | number)[]は文字列か数値を要素に持つ配列を表します。」
ずんだもん「括弧でUnionをまとめてから[]を付ける記法だね。」
四国めたん「はい、混合型配列の基本形です。」
ずんだもん「宣言時に括弧を忘れないようにしよう。」
四国めたん「要素の型ガードとセットで使うと安心です。」
ずんだもん「(string | number)[]を正しく使ってね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 宣言 */
const tokens: (string | number)[] = ["GET", 200];

/** Example 2: 関数引数 */
function handle(values: (string | number)[]) {
  values.forEach((value) => console.log(value));
}

/** Example 3: 推論 */
const inferred = ["ok", 1]; // (string | number)[]
```
