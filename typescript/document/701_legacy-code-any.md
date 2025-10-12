# #701 「レガシーコードでのany」

四国めたん「レガシーコードではanyが大量に残っていることがあります」
ずんだもん「古い設計やテスト不足で一気に直せないんだよね」
四国めたん「はい。モジュールごとに隔離し、境界でunknownやDTOを挟みましょう」
ずんだもん「並行してテスト整備とリファクタ計画を進めたいよ」
四国めたん「レガシーでもガバナンスを効かせれば段階的に安全化できます」
ずんだもん「歴史的背景を踏まえつつ改善を続けよう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: レガシー境界 */
// legacy/index.ts
export function legacyProcess(payload: any): unknown {
  return payload;
}

/** Example 2: フェンス */
import { legacyProcess } from "./legacy";
const safe = legacyProcess(payload as any); // 入口でunknown化予定

/** Example 3: 改善ボード */
const backlog = [
  { module: "legacy/auth", status: "調査中" },
  { module: "legacy/payments", status: "移行計画" },
] as const;
```
