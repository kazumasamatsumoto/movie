# #858 「演算実例」

四国めたん「BigInt演算を組み合わせた実例を見ましょう。」
ずんだもん「売上の合計と割り算で平均を出すサンプルとかいいね。」
四国めたん「はい、加算・減算・剰余をまとめて使ってみましょう。」
ずんだもん「TypeScriptの型推論でbigintが伝播する様子も確認できるよ。」
四国めたん「演算実例でBigIntの操作感を掴んでください。」
ずんだもん「計算例をコードに組み込んでみよう！」
四国めたん「演算の流れを理解すれば応用が効きます。」
ずんだもん「BigInt演算を体験してね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 合計 */
const sales = ["1000000000000000", "2300000000000000", "1500000000000000"].map(BigInt);
const total = sales.reduce((acc, cur) => acc + cur, 0n);

/** Example 2: 平均 */
const average = total / BigInt(sales.length);
const remainder = total % BigInt(sales.length);

/** Example 3: 差分 */
const diff = sales[0] - sales[1];
```
