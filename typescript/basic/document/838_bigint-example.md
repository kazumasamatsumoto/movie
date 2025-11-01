# #838 「実践例」

四国めたん「BigIntを使った実践例を確認しましょう。」
ずんだもん「分散ID生成と桁数の大きい合計を計算するサンプルがあるといいね。」
四国めたん「伝票番号をBigIntで扱う例も紹介します。」
ずんだもん「TypeScriptなら型エラーで混在を防げるのが強みだよ。」
四国めたん「実践例で導入イメージを固めてください。」
ずんだもん「大規模整数の扱いが怖くなくなるね！」
四国めたん「コードベースに合わせて応用してみましょう。」
ずんだもん「さあBigIntを現場に導入だ！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 分散ID生成 */
const baseTime = BigInt(Date.now());
function createId(nodeId: bigint, sequence: bigint) {
  return (baseTime << 22n) | (nodeId << 12n) | sequence;
}

/** Example 2: 大規模合計 */
const totals = ["1000000000000000000", "2500000000000000000"].map(BigInt);
const grandTotal = totals.reduce((acc, cur) => acc + cur, 0n);

/** Example 3: 伝票番号 */
interface Invoice {
  invoiceNo: bigint;
}
const invoice: Invoice = { invoiceNo: 202401010001n };
```
