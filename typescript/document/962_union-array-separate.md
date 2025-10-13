# #962 「string[] | number[]」

四国めたん「string[] | number[]は『文字列配列か数値配列のどちらか』を意味します。」
ずんだもん「(string | number)[]とは違う型なんだね。」
四国めたん「はい、要素が混在するのではなく、配列全体が切り替わります。」
ずんだもん「処理するときは配列自体の型ガードが必要だよ。」
四国めたん「使い分けを理解して意図した型を表現しましょう。」
ずんだもん「string[] | number[]の意味を押さえてね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 宣言 */
let values: string[] | number[] = ["a", "b"];
values = [1, 2];

/** Example 2: 型ガード */
if (Array.isArray(values) && typeof values[0] === "string") {
  // valuesはstring[]
}

/** Example 3: 関数 */
function normalize(list: string[] | number[]) {
  if (typeof list[0] === "string") {
    return list.join(",");
  }
  return list.reduce((acc, cur) => acc + cur, 0);
}
```
