# #700 「一時的使用としてのany」

四国めたん「バグ対応や緊急リリースで一時的にanyを入れる場面もあります」
ずんだもん「まずはサービス復旧を優先するケースだね」
四国めたん「はい。ただしフォローアップIssueと期限を必ず設定します」
ずんだもん「コードコメントで理由を書けばレビューで伝わりやすいよ」
四国めたん「一時的使用は例外であり、早急に撤去する姿勢が重要です」
ずんだもん「応急処置のまま放置しないよう気を付けよう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: コメント付きany */
// FIXME: Emergency fix, remove by 2024-06-30 (ticket #1234)
let emergencyPayload: any;

/** Example 2: フォローアップIssue */
const followUp = { id: "TS-1234", status: "ToDo", assignee: "Alice" };

/** Example 3: 退避関数 */
export const quarantine = (value: any): unknown => value;
```
