# #668 「anyが原因の問題例①」

四国めたん「実例として、anyのAPIレスポンスが本番障害につながったケースです」
ずんだもん「payload.statusを想定してたけど、実際はstatus_codeだったんだよね」
四国めたん「はい。コンパイルで検出できず、ユーザーに500エラーが返りました」
ずんだもん「unknownで受けてスキーマを検証していれば防げた事故だよ」
四国めたん「教訓として境界でanyを使わない方針が決まりました」
ずんだもん「実例から学んで再発を防ごう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 問題コード */
async function fetchStatus(): Promise<any> {
  const res = await fetch("/status");
  return res.json();
}
const status = (await fetchStatus()).status; // undefined

/** Example 2: 修正後 */
async function fetchStatusSafe(): Promise<unknown> {
  const res = await fetch("/status");
  return res.json();
}

/** Example 3: スキーマ検証 */
import { z } from "zod";
const StatusSchema = z.object({ status_code: z.number() });
const parsed = StatusSchema.parse(await fetchStatusSafe());
```
