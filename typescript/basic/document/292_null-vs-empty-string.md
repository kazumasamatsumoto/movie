# #292 「nullと空文字列」

四国めたん「nullと空文字列の違いについて学びましょう!」
ずんだもん「''とnullって同じように見えるけど?」
四国めたん「いいえ。nullはnull型、''はstring型で、型が異なります。」
ずんだもん「null === ''はfalseなんだね!」
四国めたん「その通りです。Nullish Coalescingでも動作が違います。」
ずんだもん「空文字列は有効な文字列だから??で置き換わらない?」
四国めたん「はい。null ?? "Guest"は"Guest"ですが、"" ?? "Guest"は""です。」
ずんだもん「Union型で型安全に扱うのが大事なのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 型の違い */
let a: null = null;     // null型
let b: string = "";     // string型
null === "";  // false

/** Example 2: Nullish Coalescingの動作 */
const name1 = null ?? "Guest";  // "Guest"
const name2 = "" ?? "Guest";    // "" (空文字列は有効値)

/** Example 3: 型安全性 */
// let str: string = null;  // エラー
let str: string | null = null;  // OK
```
