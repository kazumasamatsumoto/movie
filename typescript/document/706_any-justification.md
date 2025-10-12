# #706 「any使用の正当化プロセス」

四国めたん「anyを使うときは正当化プロセスを通しましょう」
ずんだもん「理由、代替案、期限、影響範囲を明文化するんだね」
四国めたん「はい。アーキテクトレビューや技術委員会で承認を得る仕組みも有効です」
ずんだもん「誰が責任を持つかを決めれば放置リスクが減るよ」
四国めたん「プロセスを守ることで例外運用が透明になります」
ずんだもん「正当化が面倒なくらいが適正利用の目安だね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 正当化テンプレート */
type Justification = {
  reason: string;
  alternatives: string[];
  expiry: string;
  owner: string;
};

/** Example 2: 承認フロー */
const approval = { reviewers: ["TechLead", "Security"], status: "pending" };

/** Example 3: コメント例 */
/* eslint-disable @typescript-eslint/no-explicit-any -- approved by TL-2024-05 */
```
