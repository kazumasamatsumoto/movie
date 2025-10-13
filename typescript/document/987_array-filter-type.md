# #987 「filterの型」

四国めたん「filterはコールバックが真を返す要素だけ残した新しい配列を返します。」
ずんだもん「戻り値の型はもとの配列と同じT[]だね。」
四国めたん「はい、ただし型述語を使えばより狭い型を得られます。」
ずんだもん「コールバックの戻り値型はbooleanか型述語のどちらかだよ。」
四国めたん「filterの型を活かして安全に配列を絞り込みましょう。」
ずんだもん「型述語との組み合わせがポイントだね！」

---

## 📺 画面表示用コード

```typescript
const values = ["ok", 200, "ng"];

/** Example 1: boolean戻り値 */
const onlyStrings = values.filter((value) => typeof value === "string"); // (string | number)[]

/** Example 2: 型述語 */
const strings = values.filter((value): value is string => typeof value === "string"); // string[]

/** Example 3: カスタム */
function isPositive(value: number): value is number {
  return value > 0;
}
const positives = [1, -1, 2].filter(isPositive);
```
