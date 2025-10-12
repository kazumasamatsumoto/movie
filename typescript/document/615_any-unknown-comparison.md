# #615 「anyとunknownの比較まとめ」

四国めたん「anyとunknownを比較して特性を整理しましょう」
ずんだもん「anyは自由だけど危険、unknownは安全だけど制約があるんだよね」
四国めたん「はい。代入は同じく自由ですが、操作可否が大きな違いです」
ずんだもん「プロジェクトの標準はunknown、例外的にanyと覚えておこう」
四国めたん「比較表を作るとチームにも共有しやすいですよ」
ずんだもん「メリット・デメリットを理解して使い分けよう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 特性比較 */
const comparison = {
  assignable: "any ✅ / unknown ✅",
  access: "any ✅ / unknown ❌",
  safety: "any ❌ / unknown ✅",
} as const;

/** Example 2: any使用例 */
let legacy: any = "text";
legacy = 123;

/** Example 3: unknown使用例 */
let modern: unknown = "text";
if (typeof modern === "string") modern.toUpperCase();
```
