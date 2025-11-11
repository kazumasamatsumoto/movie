# #301 「存在しないプロパティ」

四国めたん「存在しないプロパティについて学びましょう!」
ずんだもん「定義されていないプロパティにアクセスするとどうなる?」
四国めたん「はい。TypeScriptではコンパイルエラーになります。」
ずんだもん「user.ageでageが定義されてないとエラーなんだね!」
四国めたん「その通りです。オプショナルチェーンで安全にアクセスできます。」
ずんだもん「?.を使うとundefinedになるの?」
四国めたん「はい。user?.profile?.ageのようにチェーンできます。」
ずんだもん「型定義でage?:numberと書けば、安全に扱えるのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 存在しないプロパティ */
const user = { name: "Alice" };
// user.age;  // エラー: プロパティ'age'は存在しない

/** Example 2: オプショナルチェーン */
const age = user?.profile?.age;
// profileが存在しない場合はundefined

/** Example 3: 型定義で安全に */
interface User {
  name: string;
  age?: number;  // オプショナル
}
const user: User = { name: "Alice" };
user.age;  // number | undefined
```
