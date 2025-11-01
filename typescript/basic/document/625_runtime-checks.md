# #625 「ランタイムチェックの重要性」

四国めたん「unknownを安全に扱うにはランタイムチェックが欠かせません」
ずんだもん「型はコンパイル時、チェックは実行時って役割分担だね」
四国めたん「はい。guard関数、スキーマ、assertで実行時保証を加えます」
ずんだもん「複雑なデータでもチェックがあれば安心だよ」
四国めたん「ランタイムチェックを自動テストと合わせて運用しましょう」
ずんだもん「型と実行時の両輪で安全性を確保しよう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: ガード */
const isStringArray = (value: unknown): value is string[] =>
  Array.isArray(value) && value.every((item) => typeof item === "string");

/** Example 2: スキーマ */
import { z } from "zod";
const ConfigSchema = z.object({ featureFlag: z.boolean() });

/** Example 3: assert */
function assert(condition: unknown, message: string): asserts condition {
  if (!condition) throw new Error(message);
}
```
