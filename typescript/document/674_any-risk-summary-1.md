# #674 「any危険性まとめ①」

四国めたん「anyの危険性を前半でまとめましょう」
ずんだもん「ランタイムエラー、型チェック無効化、伝播、IDE支援喪失が大きいね」
四国めたん「はい。これらは即時に開発体験を悪化させます」
ずんだもん「unknownに変えるだけで多くのリスクを抑えられるよ」
四国めたん「まずは目に見える危険を排除することが優先です」
ずんだもん「今日からany削減を始めよう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: リスク一覧 */
const risks = ["runtime error", "no compile check", "propagation", "no IDE help"] as const;

/** Example 2: 対策チェック */
const mitigations = {
  runtime: "unknown+guard",
  compile: "noImplicitAny",
  propagation: "DTO mapping",
  ide: "strict typing",
} as const;

/** Example 3: Todo表 */
const todo = [
  { item: "API response unknown化", owner: "A" },
  { item: "Lint設定強化", owner: "B" },
] as const;
```
