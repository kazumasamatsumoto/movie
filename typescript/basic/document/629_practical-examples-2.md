# #629 「実践例集②」

四国めたん「実践例の第二弾でサービス層やワーカーを見てみましょう」
ずんだもん「サービスから返るunknownをDTOへ、ワーカー通信も安全にするんだね」
四国めたん「はい。型ガードとZodを使って堅牢に変換します」
ずんだもん「ロギングにもunknownを活用すると情報が失われないよ」
四国めたん「複雑な構成でもunknownを軸にすれば安全性を維持できます」
ずんだもん「実務で使う姿を具体的にイメージしよう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: サービス層 */
async function getProfile(): Promise<unknown> {
  return fetch("/api/profile").then((res) => res.json());
}

/** Example 2: Zod変換 */
import { z } from "zod";
const ProfileSchema = z.object({ id: z.number(), mail: z.string().email() });
const profile = ProfileSchema.parse(await getProfile());

/** Example 3: ワーカー通信 */
postMessage({ type: "ready" } satisfies unknown);
```
