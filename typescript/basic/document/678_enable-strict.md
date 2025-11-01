# #678 「strictモードを有効化」

四国めたん「strictモードをオンにするとany排除のチェックが一気に強化されます」
ずんだもん「noImplicitAnyだけじゃなくstrictNullChecksなどもセットになるんだね」
四国めたん「はい。既存プロジェクトでは部分的strictオプションから段階的に移行します」
ずんだもん「strictを最終ゴールに設定してロードマップを引こう」
四国めたん「コンパイラに頼れる範囲が広がるのが最大のメリットです」
ずんだもん「型安全な開発の土台を整えよう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: strict設定 */
{
  "compilerOptions": {
    "strict": true
  }
}

/** Example 2: 段階導入 */
const strictSteps = ["noImplicitAny", "strictNullChecks", "strictBindCallApply"] as const;

/** Example 3: 影響検証 */
// npx tsc --noEmit --pretty false
```
