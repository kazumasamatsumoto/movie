# #291 「nullと0の違い」

四国めたん「nullと0の違いについて学びましょう!」
ずんだもん「どちらも何もない感じだけど、違うの?」
四国めたん「はい。nullはnull型、0はnumber型で、型が異なります。」
ずんだもん「null === 0はfalseになるんだね!」
四国めたん「その通りです。Nullish Coalescingでも動作が異なります。」
ずんだもん「0は有効な数値だから??演算子で置き換わらないの?」
四国めたん「はい。0は有効値なので、null ?? 10は10ですが、0 ?? 10は0です。」
ずんだもん「型安全性を保つためにUnion型で明示的に扱うのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 型の違い */
let a: null = null;   // null型
let b: number = 0;    // number型
null === 0;  // false

/** Example 2: Nullish Coalescingの動作 */
const count1 = null ?? 10;  // 10
const count2 = 0 ?? 10;     // 0 (0は有効値)

/** Example 3: 型安全性 */
// let num: number = null;  // エラー
let num: number | null = null;  // OK
```
