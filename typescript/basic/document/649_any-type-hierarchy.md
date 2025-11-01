# #649 「型階層におけるany」

四国めたん「型階層ではunknownがトップ型、neverがボトム型です」
ずんだもん「でもanyは型階層の外側で特別扱いなんだよね」
四国めたん「はい。anyはどの型にも代入可能で、どの型からも代入を受け入れます」
ずんだもん「型理論に従わない例外だからこそ慎重に扱わないといけないんだ」
四国めたん「階層の外にいる存在だと意識して設計しましょう」
ずんだもん「理論を理解して使えば型文化がもっと強くなるね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 型階層イメージ */
const hierarchy = {
  top: "unknown",
  exception: "any",
  bottom: "never",
} as const;

/** Example 2: 代入の自由 */
let valueAny: any = 1;
let valueUnknown: unknown = valueAny;
let valueNumber: number = valueAny;

/** Example 3: neverとの比較 */
function impossible(): never {
  throw new Error("never");
}
const leak: any = impossible(); // anyは階層外
```
