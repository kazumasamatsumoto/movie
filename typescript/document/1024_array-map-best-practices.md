# #1024 「ベストプラクティス」

四国めたん「mapを使うときのベストプラクティスを押さえておきましょう。」
ずんだもん「副作用を避ける、戻り値の型を意識する、undefinedはfilterで除去する、だったね。」
四国めたん「はい、チェーンで読みやすく保ちつつ、必要なら中間結果に名前を付けます。」
ずんだもん「変換ロジックは関数に切り出すとテストしやすいよ。」
四国めたん「ベストプラクティスを守ってmapを安全に活用してください。」
ずんだもん「綺麗な変換コードを書こう！」

---

## 📺 画面表示用コード

```typescript
const values = ["1", "", "3"];

/** Example 1: 副作用なし */
const numbers = values.map((value) => Number(value));

/** Example 2: undefinedの除去 */
const compact = values
  .map((value) => (value ? Number(value) : undefined))
  .filter((value): value is number => value !== undefined);

/** Example 3: 関数抽出 */
const toLabel = (value: number) => `value:${value}`;
const labels = numbers.map(toLabel);
```
