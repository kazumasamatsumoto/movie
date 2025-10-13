# #874 「ベストプラクティス」

四国めたん「bigint比較のベストプラクティスをまとめましょう。」
ずんだもん「===と<などを組み合わせて型を揃えて扱うのが基本だったね。」
四国めたん「はい、numberとの比較は明示的に型変換してから行います。」
ずんだもん「ソートや検索は比較関数を共通化するとバグを防げるよ。」
四国めたん「境界値はBigIntで定数化してドキュメントに残しましょう。」
ずんだもん「ベストプラクティスを守れば比較ロジックも安心だね。」
四国めたん「lintやユニットテストで意図しない==を防ぎましょう。」
ずんだもん「比較の設計指針をチームで共有してね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 比較関数 */
const compareBigint = (a: bigint, b: bigint) => (a < b ? -1 : a > b ? 1 : 0);

/** Example 2: 定数化 */
const MAX_ID = 1_000_000_000_000_000n;

/** Example 3: テスト */
function expectEqualBigint(actual: bigint, expected: bigint) {
  if (actual !== expected) {
    throw new Error(`expected ${expected}, got ${actual}`);
  }
}
```
