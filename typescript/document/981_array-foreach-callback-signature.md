# #981 「forEach()のコールバック型」

四国めたん「forEachのコールバック型は(value: T, index: number, array: T[]) => voidです。」
ずんだもん「ジェネリックTは配列の要素型が入るんだね。」
四国めたん「はい、型定義を読むと第三引数までしっかり型が付いています。」
ずんだもん「戻り値は使われないからPromiseを返しても待たれない点に注意しよう。」
四国めたん「型定義を把握してコールバックの責務を明確にしましょう。」
ずんだもん「コールバック型を理解してね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 型確認 */
const list = [1, 2, 3];
list.forEach((value, index, array) => {
  type Value = typeof value; // number
  type Index = typeof index; // number
  type ArrayType = typeof array; // number[]
});

/** Example 2: Promise注意 */
list.forEach(async (value) => {
  await fetch(`/logs/${value}`); // forEachは待たない
});

/** Example 3: ジェネリックヘルパー */
function forEachTyped<T>(items: T[], callback: (value: T, index: number, array: T[]) => void) {
  items.forEach(callback);
}
```
