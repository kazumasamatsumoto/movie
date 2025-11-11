# #269 「型ガードのベストプラクティス」

四国めたん「型ガードのベストプラクティスを学びましょう!」
ずんだもん「型ガードをより効果的に使う方法があるんだね!」
四国めたん「はい。型述語関数を使うとカスタム型ガードが作れます。」
ずんだもん「obj is { name: string }みたいな書き方をするの?」
四国めたん「その通りです。型安全性を高める重要なテクニックです。」
ずんだもん「早期リターンでnullチェックをするのも分かりやすいよね!」
四国めたん「はい。if (value === null) returnで処理を分けると読みやすくなります。」
ずんだもん「明示的なチェックで安全なコードが書けるのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 型述語関数の活用 */
function isUser(obj: unknown): obj is { name: string; age: number } {
  return typeof obj === 'object' && obj !== null &&
    'name' in obj && 'age' in obj;
}

/** Example 2: 早期リターン */
function process(value: string | null) {
  if (value === null) return;
  console.log(value.toUpperCase());
}

/** Example 3: 明示的なnullチェック */
if (value !== null && value !== undefined) {
  // 安全に使用
}
```
