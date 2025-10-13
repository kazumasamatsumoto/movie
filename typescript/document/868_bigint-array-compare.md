# #868 「配列の比較」

四国めたん「bigint配列を比較するときは要素ごとにチェックします。」
ずんだもん「JSON化して比較すると精度が落ちる場合があるから気を付けたいね。」
四国めたん「はい、長さと各要素の===比較で判定しましょう。」
ずんだもん「ソート済み前提なら合わせて順序も確認できるよ。」
四国めたん「ディープイコールを実装すると再利用しやすいです。」
ずんだもん「配列比較でBigIntの順序や値を正確にチェックしよう！」
四国めたん「TypedArrayではなく通常の配列を想定しています。」
ずんだもん「手続き比較で安全性を確保してね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: ディープ比較 */
function equalsBigintArray(a: bigint[], b: bigint[]): boolean {
  if (a.length !== b.length) return false;
  return a.every((value, index) => value === b[index]);
}

/** Example 2: 使用例 */
const seqA = [1n, 2n, 3n];
const seqB = [1n, 2n, 3n];
console.log(equalsBigintArray(seqA, seqB));

/** Example 3: ソートして比較 */
function equalsUnordered(a: bigint[], b: bigint[]): boolean {
  const sortedA = [...a].sort((x, y) => (x < y ? -1 : 1));
  const sortedB = [...b].sort((x, y) => (x < y ? -1 : 1));
  return equalsBigintArray(sortedA, sortedB);
}
```
