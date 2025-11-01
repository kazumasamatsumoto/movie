# #608 「anyからのマイグレーション戦略」

四国めたん「anyを減らすマイグレーション戦略を立てましょう」
ずんだもん「現状把握→優先度付け→ガイドライン作成→段階的リリースだね」
四国めたん「はい。CIでnoImplicitAnyとlintを有効にするのも重要です」
ずんだもん「変換ツールやスクリプトを活用すると効率が上がるよ」
四国めたん「変更箇所はドキュメント化してナレッジにしましょう」
ずんだもん「戦略的に進めれば大規模プロジェクトでも成功するね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 戦略チェックリスト */
const steps = [
  "anyの洗い出し",
  "優先度分類",
  "ガード共通化",
] as const;

/** Example 2: CI設定例 */
// tsconfig: { "compilerOptions": { "noImplicitAny": true } }
// eslint: "@typescript-eslint/no-explicit-any": "error"

/** Example 3: 自動置換スクリプト */
// npx ts-migrate migrate src --plugin annotate
```
