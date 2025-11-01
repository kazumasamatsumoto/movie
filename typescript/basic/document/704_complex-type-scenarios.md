# #704 「型定義が複雑すぎる場合のany」

四国めたん「型定義が極端に複雑でメンテが追いつかない場合、一時的にanyを選ぶことがあります」
ずんだもん「ジェネリクスが絡みすぎてチーム全員が理解できないケースだね」
四国めたん「はい。その場合でも最小の型表現に分解できないか検討しましょう」
ずんだもん「過度な複雑さは保守性を落とすから段階的にシンプル化していきたいよ」
四国めたん「複雑性コストと安全性コストを比較して判断するのが大切です」
ずんだもん「無理なく型を維持できるバランスを探ろう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 複雑な型の分解 */
type LegacyMap = Record<string, unknown>;
// 一時的にanyで包む: type LegacyValue = any;

/** Example 2: TODOコメント */
// TODO: simplify type expression (see design doc #456)
let complexValue: any;

/** Example 3: リファクタ計画 */
const simplificationPlan = ["調査", "型デザイン", "置き換え"] as const;
```
