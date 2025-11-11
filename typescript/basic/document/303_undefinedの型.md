# #303 「undefinedの型」

四国めたん「undefinedの型について学びましょう!」
ずんだもん「undefinedって型として使えるの?」
四国めたん「はい。undefined型があり、undefinedリテラルのみ代入できます。」
ずんだもん「typeof undefinedは"undefined"という文字列なんだね!」
四国めたん「その通りです。strictNullChecksで型安全性が高まります。」
ずんだもん「このオプションを有効にするとどうなる?」
四国めたん「はい。stringにundefinedを代入するとエラーになります。」
ずんだもん「NonNullable<T>で型からundefinedを除外できるのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: undefined型 */
let value: undefined = undefined;
type UndefinedType = undefined;
typeof undefined; // "undefined"

/** Example 2: strictNullChecks: true */
let str: string = undefined;  // エラー
let str: string | undefined = undefined;  // OK

/** Example 3: NonNullable<T>で除外 */
type Result = string | number | undefined;
type NonUndef = NonNullable<Result>;
// → string | number
```
