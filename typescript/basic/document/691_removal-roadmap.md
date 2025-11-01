# #691 「排除ロードマップの作成」

四国めたん「ロードマップを作るとany排除が長期計画として回ります」
ずんだもん「四半期ごとにゴールを決めて、達成度を追うんだね」
四国めたん「はい。依存関係や必要なリファクタも事前に整理します」
ずんだもん「マイルストーンごとにレビュー会を開くと効果的だよ」
四国めたん「ロードマップがあると経営層や他チームにも説明しやすくなります」
ずんだもん「先を見据えた計画で確実にanyを減らそう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: ロードマップモデル */
type RoadmapItem = { quarter: string; goal: string; owner: string };
const roadmap: RoadmapItem[] = [
  { quarter: "2024Q3", goal: "API境界のanyゼロ", owner: "Backend" },
];

/** Example 2: 共有ドキュメント */
const docLinks = ["Notion/AnyRemovalPlan", "Confluence/TypeSafety"] as const;

/** Example 3: マイルストーンレビュー */
const reviewMeeting = { cadence: "monthly", attendees: ["Lead", "QA", "PM"] };
```
