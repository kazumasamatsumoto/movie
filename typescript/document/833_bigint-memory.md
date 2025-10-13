# #833 「メモリ使用量」

四国めたん「bigintは値の桁数に応じてメモリを動的に確保します。」
ずんだもん「numberは固定8バイトだけどbigintは伸び縮みするんだね。」
四国めたん「はい、大きな値を扱うほどメモリと計算時間が増加します。」
ずんだもん「大量のbigintを保持する場合はメモリ使用量に注意しよう。」
四国めたん「必要なら文字列や分割保存でメモリ戦略を検討します。」
ずんだもん「パフォーマンス計測を忘れずに！」
四国めたん「bigintの強さとコストを把握して設計しましょう。」
ずんだもん「大きな整数は計算コストも意識してね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: ベンチマーク準備 */
const values = Array.from({ length: 5 }, (_, i) => 10n ** BigInt(i * 50));

/** Example 2: 粗いコスト測定 */
console.time("bigint-ops");
values.reduce((acc, v) => acc + v, 0n);
console.timeEnd("bigint-ops");

/** Example 3: 文字列保管 */
const serialized = values.map(String); // メモリを抑えるテクニック
```
