# #903 「実践例(2)」

四国めたん「別の実践例として、固定小数点での金額計算とDB連携を行います。」
ずんだもん「サーバーでBigInt換算、DBからも文字列で受けてBigIntに戻すやつだね。」
四国めたん「はい、手数料計算や残高更新をBigIntで処理します。」
ずんだもん「最後にAPIで文字列化して返せば精度が保てるよ。」
四国めたん「TypeScriptの型で金額をブランディングすると安全です。」
ずんだもん「実践例で金融処理にもBigIntが使えることを感じてね！」
四国めたん「変換関数と型をセットにした構成がポイントです。」
ずんだもん「精度維持のワークフローを定着させよう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: ブランド型 */
const CENT = 100n;
declare const MONEY: unique symbol;
type Money = bigint & { readonly [MONEY]: true };

function toMoney(amount: number): Money {
  return (BigInt(Math.round(amount * Number(CENT))) as Money);
}

/** Example 2: 手数料計算 */
function applyFee(balance: Money, feeBp: bigint): Money {
  return (balance - (balance * feeBp) / 10_000n) as Money;
}

/** Example 3: DB変換 */
function fromDb(value: string): Money {
  return BigInt(value) as Money;
}
function toApi(value: Money): { balance: string } {
  return { balance: value.toString() };
}
```
