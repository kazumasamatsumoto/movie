# #725 「代替手段まとめ」

四国めたん「anyの代替手段を総まとめしましょう」
ずんだもん「unknown、ジェネリクス、Union、型定義、ガード、アサーション、条件付き型、Utilityだったね」
四国めたん「はい。ケースに合わせて組み合わせればanyゼロの設計が実現します」
ずんだもん「実例を参考に自分のコードベースへ応用しよう」
四国めたん「代替手段を知識としてチームに共有することも重要です」
ずんだもん「anyに頼らないTypeScriptをこれからも追求しよう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 代替一覧 */
const alternatives = [
  "unknown",
  "Generics",
  "Union",
  "Type Definition",
  "Type Guards",
  "Assertions",
  "Conditional Types",
  "Utility Types",
] as const;

/** Example 2: 適用フロー */
const flow = ["調査", "代替選定", "型設計", "実装", "検証"] as const;

/** Example 3: ナレッジ共有 */
const knowledgeBase = {
  docs: ["TypeSafety/Alternatives"],
  slack: "#ts-best-practices",
  cadence: "monthly sharing",
} as const;
```
