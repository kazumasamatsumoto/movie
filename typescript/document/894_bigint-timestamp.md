# #894 「タイムスタンプ」

四国めたん「ナノ秒やピコ秒単位のタイムスタンプはBigIntで扱うと安全です。」
ずんだもん「Date.now()はミリ秒だけど、process.hrtime.bigint()ならナノ秒が取れるね。」
四国めたん「はい、差分計測やログの順序整列に役立ちます。」
ずんだもん「BigIntで保持すれば長時間運用しても桁あふれしないよ。」
四国めたん「単位変換を関数化しておくと読みやすくなります。」
ずんだもん「タイムスタンプ処理にBigIntを取り入れて精度を高めよう！」
四国めたん「ログやメトリクスの整合性が上がります。」
ずんだもん「高精度時刻管理の土台にしてね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: ナノ秒取得 */
const start = process.hrtime.bigint();
// ...処理...
const end = process.hrtime.bigint();
const elapsedNs = end - start;

/** Example 2: 単位変換 */
function nsToMs(ns: bigint): number {
  return Number(ns) / 1_000_000;
}

/** Example 3: タイムスタンプ生成 */
function timestampNs(): bigint {
  return BigInt(Date.now()) * 1_000_000n;
}
```
