# #623 「Zodでunknownを検証」

四国めたん「Zodを使えばunknownを宣言的に検証できます」
ずんだもん「スキーマを定義してparseするだけで型が確定するんだよね」
四国めたん「はい。型インフェレンスとランタイムチェックが同時に手に入ります」
ずんだもん「エラーメッセージも整ってて実務で便利だよ」
四国めたん「anyからの移行でもZodは強力な武器になります」
ずんだもん「型安全なAPIクライアントに早変わりだね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: スキーマ定義 */
import { z } from "zod";
const UserSchema = z.object({ id: z.number(), name: z.string() });

/** Example 2: 検証 */
const payload: unknown = JSON.parse('{ "id": 1, "name": "Zun" }');
const user = UserSchema.parse(payload); // userは推論済み

/** Example 3: セーフパース */
const result = UserSchema.safeParse(payload);
if (result.success) console.log(result.data.name);
```
