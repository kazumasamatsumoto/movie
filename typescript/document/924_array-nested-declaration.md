# #924 「nested宣言」

四国めたん「配列の配列を宣言するにはネストした型を使います。」
ずんだもん「number[][]やArray<Array<number>>だね。」
四国めたん「要素がさらに配列であることを型で明示できます。」
ずんだもん「2次元以上も同じ規則で書けるよ。」
四国めたん「ネストを理解すると多次元データを型安全に扱えます。」
ずんだもん「nested宣言の書き方を覚えてね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: number[][] */
const table: number[][] = [[1, 2], [3, 4]];

/** Example 2: Array<Array<string>> */
const grid: Array<Array<string>> = [["A", "B"], ["C", "D"]];

/** Example 3: 3次元 */
const cube: number[][][] = [[[1], [2]], [[3], [4]]];
```
