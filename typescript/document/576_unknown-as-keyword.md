# #576 「asキーワードで扱うunknown」

四国めたん「asキーワードはunknownを具体的な型に変換する手段です」
ずんだもん「as stringみたいに書けるけど乱用は危険なんだよね」
四国めたん「根拠を示せる場面だけに絞るのが鉄則です」
ずんだもん「zodやio-tsで検証した後なら安心感があるよ」
四国めたん「多段アサーションは極力避けてください」
ずんだもん「テストとセットで安全に使おう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 単純アサーション */
const value: unknown = "hello";
const text = value as string;
console.log(text.length);

/** Example 2: ライブラリ検証後 */
import { z } from "zod";
const schema = z.object({ id: z.number() });
const parsed = schema.parse({ id: 1 }) as { id: number };

/** Example 3: 二重アサーション禁止例 */
// const risky = value as unknown as number; // ❌ 避ける
```
