# #862 「bigintとnumberの== - 可能」

四国めたん「==演算子ではbigintとnumberを比較できます。」
ずんだもん「10n == 10はtrueになるんだね。」
四国めたん「JavaScriptが暗黙変換して比較します。」
ずんだもん「でも精度の違いを考えると===を使った方が安全だよ。」
四国めたん「==は互換性のためだけに使い、基本は避けましょう。」
ずんだもん「TypeScriptでもlintで禁止にするのが良さそうだね。」
四国めたん「ルーズ比較は慎重に扱いましょう。」
ずんだもん「==を使うときは意図を明確にしてね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: ルーズ比較 */
console.log(10n == 10); // true

/** Example 2: 厳密比較 */
console.log(10n === 10); // false

/** Example 3: ESLint設定例 */
const eslintConfig = {
  rules: {
    eqeqeq: ["error", "always"],
  },
};
```
