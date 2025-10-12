# #705 「any使用のコストベネフィット分析」

四国めたん「anyを許容するかはコストベネフィット分析で判断します」
ずんだもん「短期開発速度と長期メンテコストを比較するんだね」
四国めたん「はい。影響範囲、リスク、代替案の工数を数字で評価しましょう」
ずんだもん「分析結果をドキュメントに残すと説明責任が果たせるよ」
四国めたん「定量化することで感覚ではなく根拠ある判断ができます」
ずんだもん「チーム全員が納得できる意思決定をしよう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 分析フォーマット */
type Analysis = {
  shortTermBenefit: string;
  longTermCost: string;
  decision: "Allow" | "Reject";
};

/** Example 2: 評価指標 */
const metrics = {
  refactorCost: 5, // 人日
  bugRisk: "High",
  customerImpact: "Medium",
} as const;

/** Example 3: ドキュメントリンク */
const docs = ["ADR-012-any-usage", "RiskLog-2024-05"] as const;
```
