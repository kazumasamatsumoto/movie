# #662 「anyでのプロパティアクセス」

四国めたん「anyにプロパティアクセスすると存在しなくても通ってしまいます」
ずんだもん「typoしたまま気付かず、本番でundefinedを参照する事故が起きるんだよね」
四国めたん「はい。プロパティを触る前に具体的な型へ変換するのが理想です」
ずんだもん「型ガードやスキーマ検証で安全性を確保しよう」
四国めたん「プロパティアクセスはunknownで守るのが鉄則です」
ずんだもん「静的保証を活かして事故を防ごう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: anyでアクセス */
const result: any = {};
console.log(result.resposne.code); // typoでもコンパイルOK

/** Example 2: ガード後アクセス */
function hasResponse(value: unknown): value is { response: { code: number } } {
  return typeof value === "object"
    && value !== null
    && "response" in value;
}

/** Example 3: スキーマ利用 */
import { z } from "zod";
const ResponseSchema = z.object({ response: z.object({ code: z.number() }) });
const safe = ResponseSchema.parse(result); // エラーで気付ける
```
