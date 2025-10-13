# #925 「number[][]の意味」

四国めたん「number[][]は『number[]の配列』を意味します。」
ずんだもん「つまり1つの要素がnumber[]になるんだね。」
四国めたん「はい、二重の[]を展開するとこうした意味が読み取れます。」
ずんだもん「二次元配列のように扱いたいときに使う型だよ。」
四国めたん「number[][]を理解して多次元データを正しく型付けしましょう。」
ずんだもん「要素の構造を意識して使ってね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: number[][] */
const matrix: number[][] = [[1, 2], [3, 4]];

/** Example 2: 1要素の型 */
const row: number[] = matrix[0];

/** Example 3: 要素アクセス */
const cell: number = matrix[1][0];
```
