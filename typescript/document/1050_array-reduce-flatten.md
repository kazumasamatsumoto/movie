# #1050 「配列の平坦化」

四国めたん「reduceで配列を平坦化する例を見てみましょう。」
ずんだもん「[[1,2],[3,4]] を [1,2,3,4] にするやつだね。」
四国めたん「はい、アキュムレータに配列を渡してconcatで結合します。」
ずんだもん「mapと組み合わせればflatMap的な処理も書けるよ。」
四国めたん「reduceで平坦化するパターンを覚えておきましょう。」
ずんだもん「flatが使えない環境でも助かるね！」

---

## 📺 画面表示用コード

```typescript
const matrix = [[1, 2], [3, 4]];

/** Example 1: concat */
const flattened = matrix.reduce<number[]>((acc, cur) => acc.concat(cur), []);

/** Example 2: スプレッド */
const flattenedSpread = matrix.reduce<number[]>((acc, cur) => [...acc, ...cur], []);

/** Example 3: map + reduce */
const flatMapped = matrix
  .map((row) => row.map((value) => value * 2))
  .reduce<number[]>((acc, cur) => acc.concat(cur), []);
```
