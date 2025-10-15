# #1045 「初期値型」

四国めたん「reduceの初期値型は結果の型に直結します。」
ずんだもん「初期値にstringを渡せば結果もstringになるんだね。」
四国めたん「はい、初期値を省略すると要素型Tが初期値として使われます。」
ずんだもん「意図しない型にならないよう初期値を明示しよう。」
四国めたん「初期値型のコントロールを身につけてください。」
ずんだもん「型設計の基本だよ！」

---

## 📺 画面表示用コード

```typescript
const values = [1, 2, 3];

/** Example 1: string初期値 */
const list = values.reduce((acc, cur) => `${acc},${cur}`, "");

/** Example 2: number初期値 */
const total = values.reduce((acc, cur) => acc + cur, 0);

/** Example 3: オブジェクト初期値 */
const summary = values.reduce<{ sum: number; count: number }>((acc, cur) => ({
  sum: acc.sum + cur,
  count: acc.count + 1,
}), { sum: 0, count: 0 });
```
