# #888 「制約実例」

四国めたん「BigInt制約に遭遇する実例を見ましょう。」
ずんだもん「JSON.stringifyで失敗、Math.maxが使えない、Decimal計算ができない、みたいなケースだね。」
四国めたん「はい、それぞれの回避策も合わせて示します。」
ずんだもん「現実のコードで起きる問題を知っておくと対策が立てやすいよ。」
四国めたん「テストで制約を再現し、対策コードも書いておきましょう。」
ずんだもん「制約実例をチームに共有してBigInt導入をスムーズにしよう！」
四国めたん「モジュール化された対策を準備してください。」
ずんだもん「制限を理解したうえで活用してね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: JSON.stringify失敗 */
function fails() {
  return JSON.stringify({ id: 1n });
}

/** Example 2: Math.max代替 */
function maxBigint(values: bigint[]): bigint {
  return values.reduce((max, cur) => (cur > max ? cur : max));
}

/** Example 3: 小数計算 */
function multiplyWithScale(amount: bigint, scale: bigint, factor: number) {
  const scaled = Number(amount) / Number(scale) * factor;
  return BigInt(Math.round(scaled * Number(scale)));
}
```
