# #946 「混合型配列とは」

四国めたん「混合型配列は異なる型の要素を一つの配列にまとめたものです。」
ずんだもん「TypeScriptではUnion型を使って表現するんだね。」
四国めたん「(string | number)[]のように指定します。」
ずんだもん「場面によってはタプルの方が適切なこともあるから注意しよう。」
四国めたん「混合型配列の特徴を理解して活用しましょう。」
ずんだもん「まずは概要を掴んでね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: Union配列 */
const tokens: (string | number)[] = ["start", 0, "stop"];

/** Example 2: 型注釈 */
let events: Array<string | number> = [];

/** Example 3: 推論 */
const mixed = ["ok", 200]; // (string | number)[]
```
