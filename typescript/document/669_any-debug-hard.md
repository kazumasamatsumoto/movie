# #669 「anyでデバッグが困難になった例」

四国めたん「別の実例ではanyがデバッグ時間を大幅に増やしました」
ずんだもん「ログに出るはずのプロパティがundefinedで、原因追跡に数時間かかったんだよね」
四国めたん「はい。型が無いのでIDEで参照先を追えず、手作業で探ることになりました」
ずんだもん「unknownでガードを書いていれば即座にエラーに気付けたよ」
四国めたん「デバッグ効率も型安全性に依存していると実感できます」
ずんだもん「再発防止でanyを段階的に排除したいね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: anyログ */
const payload: any = { };
console.log("user", payload.user.id); // undefined

/** Example 2: デバッグ補助 */
function logUnknown(value: unknown) {
  console.log("type", typeof value, "keys", value && typeof value === "object" ? Object.keys(value) : []);
}

/** Example 3: 型ガード導入 */
const isUser = (value: unknown): value is { user: { id: string } } =>
  typeof value === "object" && value !== null && "user" in value;
```
