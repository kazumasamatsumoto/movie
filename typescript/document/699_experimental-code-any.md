# #699 「実験的コードでのany」

四国めたん「実験的コードでは仕様が固まるまでanyで柔軟に扱うことがあります」
ずんだもん「研究開発チームが検証している段階だと型を決めにくいからね」
四国めたん「はい。結果が有望なら本線に取り込む段階で型を定義します」
ずんだもん「実験コードには明確なラベルとドキュメントを付けよう」
四国めたん「anyを使う理由と終了条件を明文化するのが重要です」
ずんだもん「実験が終わったらすぐ型安全な実装に移行しよう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: experimental flag */
const experiment = {
  status: "prototype",
  owner: "R&D",
  retiresAt: "2024-08-01",
} as const;

/** Example 2: anyで柔軟に */
export const evaluate = (value: any): { score: number } => {
  // 仮実装
  return { score: Math.random() };
};

/** Example 3: 移行条件 */
const promotionCriteria = ["結果が安定", "仕様確定", "型設計レビュー"] as const;
```
