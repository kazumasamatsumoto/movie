# #708 「期限付きany運用」

四国めたん「anyを許容するなら必ず撤去期限を設定しましょう」
ずんだもん「過ぎたらCIで失敗させる仕組みがあると良いよね」
四国めたん「はい。期限違反のanyはアラートを上げて優先的に対処します」
ずんだもん「JiraやIssueのdue dateと連動させると管理が楽だよ」
四国めたん「期限付き運用で例外を確実にクローズできます」
ずんだもん「未来の自分を助けるためにも期限を守ろう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 期限コメント */
// TEMP(any) remove by 2024-07-15 (issue TS-1200)
let temporaryValue: any;

/** Example 2: CIチェック */
// scripts/check-any-deadline.ts
// 期限超過コメントを検出してexit 1

/** Example 3: アラート設定 */
const alert = { channel: "#type-safety", frequency: "daily" };
```
