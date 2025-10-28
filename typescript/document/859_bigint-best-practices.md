# #859 「ベストプラクティス」

四国めたん「bigint演算のベストプラクティスを整理しましょう。」
ずんだもん「型は揃えて、必要な場面だけNumber()やBigInt()で変換するんだったね。」
四国めたん「演算前後の単位と範囲を明確にしましょう。」
ずんだもん「文字列との変換やJSON対応も事前に設計するのが大事だよ。」
四国めたん「桁数が大きい演算はベンチマークしてパフォーマンスを確認します。」
ずんだもん「ベストプラクティスを守って安全なBigInt演算を実現しよう！」
四国めたん「ドキュメント化とユニットテストも合わせて行ってください。」
ずんだもん「チーム全体でBigIntの使い方を揃えよう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 型ガード */
function ensureBigint(value: number | bigint): bigint {
  return typeof value === "bigint" ? value : BigInt(value);
}

/** Example 2: 単位管理 */
const MILLI = 1_000n;
const MICRO = 1_000_000n;

/** Example 3: JSON用ラッパー */
function serializeBigint(value: bigint) {
  return { value: value.toString() };
}
```
