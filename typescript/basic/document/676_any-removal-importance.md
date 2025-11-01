# #676 「any排除の重要性」

四国めたん「anyを排除することは型安全と品質維持に直結します」
ずんだもん「放置するとバグも技術的負債も増えるからね」
四国めたん「はい。静的保証を取り戻すためにも優先度の高い取り組みです」
ずんだもん「チーム全体で共通認識を持って計画的に進めたいよ」
四国めたん「排除は開発体験を改善し、長期的なコストを抑えます」
ずんだもん「まずは重要性を共有してムーブメントを作ろう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: any排除の効果チェック */
const benefits = {
  runtimeSafety: "向上",
  refactorAbility: "改善",
  onboarding: "容易",
} as const;

/** Example 2: any検出の初期数 */
const metrics = { anyCountBefore: 120, anyCountAfter: 5 };

/** Example 3: TODO化 */
const removalCampaign = [
  "any一覧の可視化",
  "境界のunknown化",
  "DTO作成",
] as const;
```
