# #866 「ソート」

四国めたん「bigintの配列をソートするときは比較関数で型を揃えましょう。」
ずんだもん「Array.prototype.sortはデフォルトだと文字列比較だから注意だね。」
四国めたん「はい、(a, b) => (a < b ? -1 : 1) のように比較します。」
ずんだもん「大きなビット数でも正確に順序付けできるよ。」
四国めたん「numberと混ざった配列は事前に変換しておきます。」
ずんだもん「ソート時にtoStringしないよう気をつけよう！」
四国めたん「比較関数でBigIntの順序を安定させましょう。」
ずんだもん「ソートのベストプラクティスを守ってね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 基本ソート */
const values = [3n, 1n, 10n];
values.sort((a, b) => (a < b ? -1 : a > b ? 1 : 0));

/** Example 2: 降順 */
values.sort((a, b) => (a > b ? -1 : a < b ? 1 : 0));

/** Example 3: numberをBigIntへ変換 */
const mixed = [1, 2n, 3];
const normalized = mixed.map((v) => (typeof v === "bigint" ? v : BigInt(v))).sort((a, b) => (a < b ? -1 : 1));
```
