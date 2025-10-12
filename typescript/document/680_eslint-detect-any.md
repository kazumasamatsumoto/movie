# #680 「ESLintでanyを検出」

四国めたん「ESLintのno-explicit-anyルールでanyを自動検出できます」
ずんだもん「@typescript-eslint/no-explicit-anyをerrorにするんだよね」
四国めたん「はい。--max-warnings 0を付ければCIで必ず失敗させられます」
ずんだもん「tsconfigとの設定差異も含めてCIのフローに組み込もう」
四国めたん「ESLintは自動修正提案のメッセージも出せるので学習効果があります」
ずんだもん「開発時にanyを即座に検知できる環境を整えよう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: ESLint設定 */
// .eslintrc.cjs
module.exports = {
  rules: {
    "@typescript-eslint/no-explicit-any": "error",
  },
};

/** Example 2: CLI */
// npx eslint "src/**/*.ts" --max-warnings 0

/** Example 3: IDE連携 */
const eslintSettings = {
  "eslint.validate": ["typescript", "typescriptreact"],
};
```
