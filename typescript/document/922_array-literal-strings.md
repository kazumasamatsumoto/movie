# #922 「["a", "b"]の型」

四国めたん「["a", "b"]のような文字列配列はstring[]に推論されます。」
ずんだもん「constで宣言してもstring[]のままだよね。」
四国めたん「はい、要素を固定したいときはas constでreadonly ["a", "b"]にします。」
ずんだもん「タグやカテゴリを列挙するときに便利だよ。」
四国めたん「リテラル型にしたい場面とstring[]で十分な場面を使い分けましょう。」
ずんだもん「推論を理解して意図した型を得てね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 推論 */
const labels = ["todo", "doing", "done"]; // string[]

/** Example 2: as const */
const statuses = ["todo", "doing", "done"] as const; // readonly ["todo", ...]

/** Example 3: 型注釈 */
const names: string[] = ["meta", "zunda"];
```
