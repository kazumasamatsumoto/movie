# #672 「anyが引き起こすセキュリティリスク」

四国めたん「anyはセキュリティ面でもリスクになります」
ずんだもん「入力検証を飛ばして任意の値をevalに渡しちゃうかもしれないんだよね」
四国めたん「はい。型が無いと危険な値のチェックを忘れがちになります」
ずんだもん「unknownで受けてバリデーションすれば不正データを弾けるよ」
四国めたん「型安全はセキュリティ対策の一部と考えましょう」
ずんだもん「anyを放置しないことが防御の第一歩だね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: anyで危険な操作 */
const payload: any = JSON.parse(input);
eval(payload.script); // 任意コード実行

/** Example 2: unknown＋バリデーション */
const safePayload: unknown = JSON.parse(input);
if (typeof safePayload === "object" && safePayload !== null && "script" in safePayload) {
  throw new Error("script execution forbidden");
}

/** Example 3: スキーマ検証 */
import { z } from "zod";
const SafeSchema = z.object({ action: z.enum(["read", "write"]) });
const safe = SafeSchema.safeParse(JSON.parse(input));
```
