# #696 「段階的移行でのany許容」

四国めたん「段階的移行では一時的にanyを残す判断も必要です」
ずんだもん「すべてを一度に直せない大規模コードだと仕方ないよね」
四国めたん「はい。ロードマップと期限を明示しながら、安全な境界で囲い込みます」
ずんだもん「移行ステップを記録して後戻りを防ごう」
四国めたん「段階移行でもガバナンスを効かせればリスクをコントロールできます」
ずんだもん「計画的な許容でスムーズに移行しよう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 移行フラグ */
type MigrationState = "legacy-any" | "unknown" | "typed";
const modules: Record<string, MigrationState> = {};

/** Example 2: 許容コメント */
// TODO: replace legacy any by 2024-09-01
let interim: any;

/** Example 3: リスク境界 */
const boundary = (value: any): unknown => value; // 周辺でunknown化
```
