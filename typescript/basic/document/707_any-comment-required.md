# #707 「any使用時のコメント必須化」

四国めたん「anyを使う場合はコメントで理由と期限を必須にしましょう」
ずんだもん「eslintルールでコメントが無いanyを検出できるんだよね」
四国めたん「はい。TODOとIssue番号を添える運用にすると管理しやすいです」
ずんだもん「コードレビューでコメントが無いanyは自動で弾きたいよ」
四国めたん「可視化されることで例外が適切に扱われます」
ずんだもん「コメント文化でanyをコントロールしよう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: コメント付きany */
// TODO(TS-999): remove any after schema update
let temporaryResult: any;

/** Example 2: ESLintカスタムルール */
// ESLint pluginでコメントの有無をチェックする例を記載

/** Example 3: PRテンプレート */
const template = [
  "- [ ] any使用箇所に理由コメントあり",
  "- [ ] Issueリンクを記載",
] as const;
```
