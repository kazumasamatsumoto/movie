# #1014 「コールバック引数」

四国めたん「mapのコールバックにはvalue, index, arrayの3つの引数があります。」
ずんだもん「必要なものだけ受け取ればいいんだね。」
四国めたん「はい、未使用の引数は省略しても問題ありません。」
ずんだもん「indexが欲しいときは第二引数で受け取ろう。」
四国めたん「引数の型はlib.d.tsで定義されている通りです。」
ずんだもん「コールバック引数を上手に使ってね！」

---

## 📺 画面表示用コード

```typescript
const items = ["meta", "zunda"];

/** Example 1: valueのみ */
items.map((value) => value.toUpperCase());

/** Example 2: value + index */
items.map((value, index) => `${index}:${value}`);

/** Example 3: array参照 */
items.map((value, index, array) => `${value}/${array.length}`);
```
