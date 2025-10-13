# #915 「使い分け」

四国めたん「Array<T>とT[]はプロジェクトのコーディング規約に合わせて使い分けます。」
ずんだもん「ReactのJSX多めならArray<T>、バックエンドならT[]が多い印象だね。」
四国めたん「はい、リンター設定で統一するチームもあります。」
ずんだもん「可読性を保つために場面ごとのベストチョイスを決めておこう。」
四国めたん「混在する場合はレビューで揃えていくのが理想です。」
ずんだもん「使い分けルールを決めて型表現を整理しよう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: ESLint設定 */
// "@typescript-eslint/array-type": ["error", { default: "array-simple" }]

/** Example 2: フロントエンド */
const components: Array<React.ReactNode> = [];

/** Example 3: バックエンド */
const ids: string[] = ["u01", "u02"];
```
