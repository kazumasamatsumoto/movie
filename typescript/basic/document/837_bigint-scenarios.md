# #837 「使用場面」

四国めたん「現場での具体的な使用場面をイメージしましょう。」
ずんだもん「金融システムの残高やレガシーDBのbigint列が典型だよね。」
四国めたん「繰越計算や累積カウンタでもBigIntが重宝します。」
ずんだもん「APIレスポンスで文字列になっているIDをBigIntに戻す場面もあるね。」
四国めたん「また、ログの行数やアクセス数を正確に集計するときにも便利です。」
ずんだもん「使用場面を想定して型を設計するとスムーズだよ。」
四国めたん「BigIntの採用ポイントをチームと共有しましょう。」
ずんだもん「どこで使うかを明確にした上で導入してね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: DBのBigInt列 */
interface AccountRow {
  id: bigint;
  balance: bigint;
}

/** Example 2: APIレスポンス復元 */
function parseId(value: string): bigint {
  return BigInt(value);
}

/** Example 3: カウンタ */
let totalRequests: bigint = 0n;
function record() {
  totalRequests += 1n;
}
```
