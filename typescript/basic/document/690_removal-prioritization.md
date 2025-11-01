# #690 「排除の優先順位付け」

四国めたん「any排除は影響度と頻度で優先順位を付けましょう」
ずんだもん「ユーザー向け処理や共通ライブラリのanyから着手するんだね」
四国めたん「はい。バグリスクの高いI/O境界を最優先にします」
ずんだもん「優先度マトリクスを作ると合意形成しやすいよ」
四国めたん「優先順位が明確だとスプリント計画も立てやすくなります」
ずんだもん「効果の大きいところから攻めよう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 優先度マトリクス */
type Priority = "High" | "Medium" | "Low";
const priorityMatrix: Record<Priority, string[]> = {
  High: ["API Controllers", "Public SDK"],
  Medium: ["Internal services"],
  Low: ["Test helpers"],
};

/** Example 2: スコアリング */
const score = (impact: number, frequency: number) => impact * 0.6 + frequency * 0.4;

/** Example 3: Jiraのラベル設定 */
const labels = ["any-removal", "high-risk", "boundary"] as const;
```
