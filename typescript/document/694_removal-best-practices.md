# #694 「any排除ベストプラクティス」

四国めたん「any排除のベストプラクティスを確認しましょう」
ずんだもん「検出→unknown化→適切な型→検証の流れをテンプレ化するんだね」
四国めたん「はい。LintとCIで新規混入を防ぎ、ナレッジ共有を徹底します」
ずんだもん「ガードとDTOの共通ライブラリを作ると効率が上がるよ」
四国めたん「定期的なレビュー会で進行状況を振り返りましょう」
ずんだもん「プラクティスを守ってanyのないコードベースを維持しよう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: ワークフローチェックリスト */
const workflow = ["Detect", "Replace with unknown", "Introduce DTO", "Validate"] as const;

/** Example 2: 共通ライブラリ */
export const isRecord = (value: unknown): value is Record<string, unknown> =>
  typeof value === "object" && value !== null;

/** Example 3: レビュー項目 */
const reviewChecklist = [
  "ガード追加済みか",
  "DTOがドキュメント化されているか",
  "テストが更新されているか",
] as const;
```
