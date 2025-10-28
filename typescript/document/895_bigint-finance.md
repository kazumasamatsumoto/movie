# #895 「金額計算」

四国めたん「金額計算ではBigIntによる固定小数点が有効です。」
ずんだもん「通貨を最小単位で保持すれば丸め誤差がなくなるね。」
四国めたん「例えば円なら1円単位、ドルならセントや最小刻みで表現します。」
ずんだもん「VATや手数料を計算するときもBigIntで精度を確保しよう。」
四国めたん「結果を表示するときだけ小数点を入れてフォーマットします。」
ずんだもん「金融システムの安全性が上がるね！」
四国めたん「複利計算など大きな数値も正確に取り扱えます。」
ずんだもん「金額計算にBigIntを導入してバグを減らそう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 固定小数点 */
const CENT = 100n;
function dollarsToCents(amount: number): bigint {
  return BigInt(Math.round(amount * Number(CENT)));
}

/** Example 2: VAT (basis points) */
const BASIS_POINTS = 10_000n; // 100% = 10000bp
function addVat(amount: bigint, rateBp: bigint): bigint {
  return amount + (amount * rateBp) / BASIS_POINTS;
}

/** Example 3: 表示 */
function formatCents(value: bigint): string {
  const dollars = value / CENT;
  const cents = value % CENT;
  return `${dollars}.${cents.toString().padStart(2, "0")}`;
}
```
