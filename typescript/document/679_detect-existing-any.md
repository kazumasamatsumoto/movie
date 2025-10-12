# #679 「既存anyの検出方法」

四国めたん「既存のanyを洗い出すには検索と静的解析を組み合わせます」
ずんだもん「rg \"any\" やtscの診断、TS ASTツールも使えるね」
四国めたん「はい。eslint --print-configでno-explicit-anyの対象も確認できます」
ずんだもん「検出結果をスプレッドシートにまとめると管理しやすいよ」
四国めたん「可視化が排除プロジェクトの第一ステップです」
ずんだもん「全体像を掴んで優先順位を決めよう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: ripgrepで検索 */
// rg --line-number "any" src

/** Example 2: tsc診断 */
// npx tsc --noEmit --pretty false | rg "implicitly has an 'any' type"

/** Example 3: 集計表フォーマット */
type AnyOccurrence = { file: string; line: number; note?: string };
const findings: AnyOccurrence[] = [];
```
