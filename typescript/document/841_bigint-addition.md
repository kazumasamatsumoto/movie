# #841 「加算 - a + b」

四国めたん「bigintの加算はnumberと同じく+演算子を使います。」
ずんだもん「ただし両辺がbigintじゃないとTypeErrorになるんだよね。」
四国めたん「はい、a + bで巨大な整数の合計を精度落ちなしで求められます。」
ずんだもん「numberに変換する前提ならNumber()を挟んでね。」
四国めたん「加算は頻出なのでユーティリティ関数を用意すると便利です。」
ずんだもん「BigIntの加算で安全に合計を出そう！」
四国めたん「単位や型を揃えてから計算するのがポイントです。」
ずんだもん「足し算で精度を失わないのが嬉しいよ！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 基本加算 */
const sum = 10n + 20n;

/** Example 2: 関数化 */
function addBigInt(...values: bigint[]): bigint {
  return values.reduce((acc, cur) => acc + cur, 0n);
}

/** Example 3: numberへ変換 */
const total = Number(100n + 200n);
```
