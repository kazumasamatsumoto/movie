# #607 「any型の段階的排除」

四国めたん「any型は段階的に排除すると現場への負荷が抑えられます」
ずんだもん「モジュール単位でunknownや具象型に置き換えるんだね」
四国めたん「はい。lintで検出し、TODOリストを作って計画的に進めます」
ずんだもん「テストを揃えてから置き換えると安心だよ」
四国めたん「優先度の高い境界から着手し、成果を共有しましょう」
ずんだもん「段階的な撤廃で安全なコードベースに近づけよう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: any一覧の抽出 */
// rg "any" src --hidden

/** Example 2: 置き換えフロー */
function migrate(value: any) {
  const converted: unknown = value;
  if (typeof converted === "string") return converted;
  return String(converted);
}

/** Example 3: TODO管理 */
const migrationChecklist = [
  "APIレスポンスをunknownへ",
  "DTOを正確な型へ",
] as const;
```
