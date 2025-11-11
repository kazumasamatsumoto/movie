# #313 「有効時の挙動」

四国めたん「strictNullChecks有効時の挙動について学びましょう!」
ずんだもん「有効にするとどうなるの?」
四国めたん「はい。nullやundefinedを代入するには、Union型で明示的に指定する必要があります。」
ずんだもん「string | null のように書かないとエラーになるんだね!」
四国めたん「その通りです。nullチェックが必須になり、安全なコードを書けます。」
ずんだもん「if文でnullチェックをすると型が絞り込まれるの?」
四国めたん「はい。Type Narrowingにより、チェック後はnullでない型として扱われます。」
ずんだもん「オプショナルプロパティは number | undefined になるのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: Union型で明示的に指定 */
// strictNullChecks: true
let name: string = null; // エラー
let name: string | null = null; // OK

/** Example 2: nullチェックが必須 */
function greet(name: string | null) {
  if (name !== null) {
    return name.toUpperCase(); // 安全
  }
  return "Guest";
}

/** Example 3: オプショナルプロパティ */
interface User {
  name: string;
  age?: number; // number | undefined
}
```
