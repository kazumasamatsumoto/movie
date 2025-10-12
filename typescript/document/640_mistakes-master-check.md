# #640 「マスターチェックで自己診断」

四国めたん「unknown運用のマスターチェックで自己診断しましょう」
ずんだもん「境界でunknownにできてる？ガードを共有してる？Lint走ってる？だね」
四国めたん「はい。チェックリスト形式でレビュー前に確認すると効果的です」
ずんだもん「定期的に棚卸しすると抜け漏れが見つかるよ」
四国めたん「マスターチェックで型安全文化を維持しましょう」
ずんだもん「チーム全体でunknownマスターになろう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: チェックリスト */
const checklist = [
  "境界でunknownを使う",
  "型ガードを共通化する",
  "Lintとテストを通す",
] as const;

/** Example 2: セルフレビュー関数 */
function ensureGuard(fn: unknown): asserts fn is () => void {
  if (typeof fn !== "function") throw new Error("guard missing");
}

/** Example 3: 定期棚卸し */
const auditLog: Array<{ item: string; ok: boolean }> = [
  { item: "unknown境界", ok: true },
  { item: "ガード共通化", ok: false },
];
```
