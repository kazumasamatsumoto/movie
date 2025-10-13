# #929 「ベストプラクティス」

四国めたん「配列型のベストプラクティスを押さえましょう。」
ずんだもん「空配列には型注釈、混在はUnionを明示、命名は複数形にするんだったね。」
四国めたん「はい、型推論に任せるか注釈するかを判断する基準も決めておきます。」
ずんだもん「メソッドチェーンでも要素型が保たれるように注意しよう。」
四国めたん「レビューで配列型が適切か確認する文化を作りましょう。」
ずんだもん「ベストプラクティスを守って配列操作を安全に！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 空配列 */
const logs: string[] = [];

/** Example 2: Union配列 */
const events: Array<{ type: "start" | "stop"; timestamp: number }> = [];

/** Example 3: ユーティリティ */
function ensureArray<T>(value: T | T[]): T[] {
  return Array.isArray(value) ? value : [value];
}
```
