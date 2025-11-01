# #990 「reduceの型」

四国めたん「reduceはアキュムレータと要素を使って一つの値に畳み込みます。」
ずんだもん「ジェネリックは<U>(callback: (acc: U, value: T, index: number, array: T[]) => U, initialValue: U) => U だね。」
四国めたん「初期値の型がアキュムレータの型を決めます。」
ずんだもん「初期値を省略すると最初の要素が初期値になるから注意しよう。」
四国めたん「reduceの型を理解して正しい集計を行いましょう。」
ずんだもん「強力な関数だから正しく使ってね！」

---

## 📺 画面表示用コード

```typescript
const numbers = [1, 2, 3];

/** Example 1: 合計 */
const sum = numbers.reduce((acc, cur) => acc + cur, 0); // number

/** Example 2: オブジェクト */
const counts = ["a", "b", "a"].reduce<Record<string, number>>((acc, cur) => {
  acc[cur] = (acc[cur] ?? 0) + 1;
  return acc;
}, {});

/** Example 3: 初期値省略 */
const withoutInit = numbers.reduce((acc, cur) => acc + cur); // 初期値省略は注意
```
