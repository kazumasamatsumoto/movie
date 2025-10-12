# #604 「anyからunknownへ移行」

四国めたん「anyをunknownへ移行すると型安全性が向上します」
ずんだもん「まず型注釈をunknownに変えてガードを追加するんだね」
四国めたん「はい。順序は置き換え→コンパイルエラー修正→テストです」
ずんだもん「eslintのno-unsafe系がエラーを示してくれるよ」
四国めたん「段階的に置き換えても効果は大きいので早めに取り組みましょう」
ずんだもん「チーム全体で移行ガイドラインを作るとスムーズだよ！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: anyからunknownへ */
let payload: unknown = getLegacyData();
// payload.id; // ❌ guard追加が必要

/** Example 2: ガード追加 */
function ensureUser(value: unknown) {
  if (typeof value === "object" && value !== null && "id" in value) {
    return (value as { id: number }).id;
  }
  throw new TypeError("invalid user");
}

/** Example 3: ESLint設定 */
// "@typescript-eslint/no-unsafe-member-access": "error"
```
