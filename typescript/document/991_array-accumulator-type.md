# #991 「アキュムレータ型」

四国めたん「reduceのアキュムレータの型は初期値で決まります。」
ずんだもん「初期値にnumberを渡せばアキュムレータもnumberなんだね。」
四国めたん「はい、ジェネリックUがアキュムレータになります。」
ずんだもん「初期値を省略すると配列要素から推論されるから注意しよう。」
四国めたん「アキュムレータ型を意識してreduceを設計してください。」
ずんだもん「型を明示すると安全だよ！」

---

## 📺 画面表示用コード

```typescript
const scores = [80, 90, 70];

/** Example 1: number */
const total = scores.reduce((acc, cur) => acc + cur, 0); // acc: number

/** Example 2: string */
const joined = scores.reduce((acc, cur) => acc + "," + cur, ""); // acc: string

/** Example 3: オブジェクト */
const stats = scores.reduce<{ sum: number; count: number }>((acc, cur) => {
  return { sum: acc.sum + cur, count: acc.count + 1 };
}, { sum: 0, count: 0 });
```
