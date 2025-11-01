# #677 「noImplicitAnyを有効化」

四国めたん「any排除の第一歩はnoImplicitAnyを必ず有効化することです」
ずんだもん「暗黙anyを禁止して新規の混入を防ぐんだね」
四国めたん「はい。既存コードが多い場合はワーニングから始めて段階的に対応します」
ずんだもん「CIでも強制すると誰かが戻す心配が減るよ」
四国めたん「設定変更だけで大きな成果が得られます」
ずんだもん「今すぐtsconfigを見直そう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: tsconfig設定 */
{
  "compilerOptions": {
    "noImplicitAny": true
  }
}

/** Example 2: エラー確認コマンド */
// npx tsc --noEmit

/** Example 3: CI統合 */
// github actions
// - run: npx tsc --noEmit
```
