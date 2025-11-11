# #314 「設定方法 - tsconfig.json」

四国めたん「strictNullChecksの設定方法について学びましょう!」
ずんだもん「tsconfig.jsonで設定するの?」
四国めたん「はい。compilerOptionsのstrictNullChecksをtrueにすることで有効化できます。」
ずんだもん「個別に設定する方法と一括で設定する方法があるんだね!」
四国めたん「その通りです。strict: trueにすると、strictNullChecksも含めた全てのstrictオプションが有効になります。」
ずんだもん「推奨されるのはどっち?」
四国めたん「はい。strict: trueを使うのが推奨されます。より安全なコードを書けます。」
ずんだもん「tsc --showConfigで設定を確認できるのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 個別設定 */
// tsconfig.json
{
  "compilerOptions": {
    "strictNullChecks": true
  }
}

/** Example 2: strict設定（推奨） */
{
  "compilerOptions": {
    "strict": true  // strictNullChecksも含まれる
  }
}

/** Example 3: 確認方法 */
tsc --showConfig
// strictNullChecksの値を確認
```
