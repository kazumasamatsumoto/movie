# #673 「anyがもたらす長期的影響」

四国めたん「anyを放置すると長期的に品質と生産性が低下します」
ずんだもん「新機能を追加するたびに不具合が混ざりやすくなるんだよね」
四国めたん「はい。新メンバーのオンボーディングも難しくなります」
ずんだもん「型が守られていれば仕様理解が早くなるのにね」
四国めたん「長期的な開発速度を守るためにもanyは段階的に排除しましょう」
ずんだもん「未来の自分のために型安全を投資しよう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 負債累積グラフ */
const debtTimeline = [
  { quarter: "Q1", anyCount: 5 },
  { quarter: "Q2", anyCount: 18 },
] as const;

/** Example 2: オンボーディングチェック */
const onboardingTasks = ["型定義確認", "ガード実装練習", "unknown運用フロー理解"] as const;

/** Example 3: 解消ロードマップ */
const roadmap = [
  "noImplicitAny ON",
  "any一覧の可視化",
  "unknown置き換え",
] as const;
```
