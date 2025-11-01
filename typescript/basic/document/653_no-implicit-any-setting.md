# #653 「noImplicitAny設定の効果」

四国めたん「noImplicitAnyを有効にすると暗黙的anyが許されなくなります」
ずんだもん「コンパイラが型注釈を要求してくれるんだよね」
四国めたん「はい。プロジェクトの型品質を底上げする基本設定です」
ずんだもん「既存コードが多いときは段階的に警告から始めてもいいよ」
四国めたん「CIで強制してany混入を防ぎましょう」
ずんだもん「設定一つで型安全性が大きく向上するね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: tsconfig設定 */
{
  "compilerOptions": {
    "noImplicitAny": true,
    "strictNullChecks": true
  }
}

/** Example 2: コンパイルエラー例 */
function parse(input) {
  return JSON.parse(input); // ❌ noImplicitAnyでエラー
}

/** Example 3: 置き換え */
function parseSafe(input: string): unknown {
  return JSON.parse(input);
}
```
