# #296 「undefined型とは」

四国めたん「undefined型について学びましょう!」
ずんだもん「undefinedってどういう時に使うの?」
四国めたん「はい。値が未定義であることを表現する型です。」
ずんだもん「オプショナルプロパティと関係がある?」
四国めたん「その通りです。name?:stringはstring | undefinedと同じ意味です。」
ずんだもん「strictNullChecksが有効だとエラーになるの?」
四国めたん「はい。number型にundefinedは代入できません。」
ずんだもん「Union型で明示的にundefinedを扱うのが安全なのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: undefined型の基本 */
let value: undefined = undefined;
let name: string | undefined;

/** Example 2: オプショナルプロパティ */
interface User {
  name?: string;  // string | undefined
  age?: number;   // number | undefined
}

/** Example 3: strictNullChecks有効時 */
// let id: number = undefined; // エラー
let id: number | undefined = undefined; // OK
```
