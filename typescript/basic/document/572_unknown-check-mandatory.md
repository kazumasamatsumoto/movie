# #572 「unknownで型チェックを義務化」

四国めたん「unknownを導入したら型チェックをチームルールにしましょう」
ずんだもん「ESLintでno-unsafe系ルールを有効にすると徹底できるね」
四国めたん「レビューでもガードやアサーションがあるか必ず確認します」
ずんだもん「テンプレートのヘルパー関数を用意するとミスが減るよ」
四国めたん「型チェック義務化がunknown活用の鍵です」
ずんだもん「安全第一の開発フローを定着させよう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: ESLint設定例 */
// "@typescript-eslint/no-unsafe-call": "error"
// "@typescript-eslint/no-unsafe-member-access": "error"

/** Example 2: ガードヘルパー */
const isObject = (value: unknown): value is Record<string, unknown> =>
  typeof value === "object" && value !== null;

/** Example 3: 安全な処理フロー */
function process(value: unknown) {
  if (!isObject(value)) return;
  console.log(value.title);
}
```
