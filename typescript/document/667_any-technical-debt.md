# #667 「anyは技術的負債になる」

四国めたん「anyを放置すると技術的負債として蓄積します」
ずんだもん「後で直そうと思っても、影響範囲が広がって手が付けにくくなるんだよね」
四国めたん「はい。マイグレーション計画と負債台帳で管理するのが重要です」
ずんだもん「スプリントごとに返済枠を設けると徐々に減らせるよ」
四国めたん「負債を定量化してチームの共通認識にしましょう」
ずんだもん「健全なコードベースを維持しようね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 負債台帳 */
const debtList = [
  { file: "legacy/api.ts", reason: "third-party SDK", plan: "replace Q3" },
] as const;

/** Example 2: 作業チケット */
const ticket = {
  title: "Replace any in paymentService",
  estimate: "2d",
} as const;

/** Example 3: マイグレーションスクリプト */
// npx ts-migrate migrate src/payment --plugin annotate
```
