# #856 「パフォーマンス」

四国めたん「bigintの演算はnumberよりも遅く、メモリも多く使います。」
ずんだもん「桁数に応じてコストが増えるってことだね。」
四国めたん「はい、ベンチマークを取りながらボトルネックを確認しましょう。」
ずんだもん「必要な箇所だけBigIntを使い、その他はnumberで済ませるのが現実的だよ。」
四国めたん「ホットパスではアルゴリズムを工夫して演算回数を減らします。」
ずんだもん「パフォーマンスを意識しながらBigIntを導入しよう！」
四国めたん「型の選択と最適化のバランスが大切です。」
ずんだもん「メトリクスを計測してチューニングしてね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: シンプルベンチ */
console.time("bigint");
let accBig = 0n;
for (let i = 0n; i < 100_000n; i++) {
  accBig += i;
}
console.timeEnd("bigint");

console.time("number");
let accNum = 0;
for (let i = 0; i < 100_000; i++) {
  accNum += i;
}
console.timeEnd("number");

/** Example 2: 条件付き使用 */
function accumulate(values: (number | bigint)[]) {
  return values.reduce((acc, cur) =>
    typeof cur === "bigint" && typeof acc === "bigint"
      ? acc + cur
      : Number(acc) + Number(cur),
  0);
}
```
