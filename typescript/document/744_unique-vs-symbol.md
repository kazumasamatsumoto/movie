# #744 「unique symbolとsymbol型」

四国めたん「unique symbolはsymbol型のリテラル版です。」
ずんだもん「だからunique symbolはsymbolに代入できるけど逆はできないんだよね。」
四国めたん「はい、unique symbolを汎用化したいときはsymbol型へワイドニングされます。」
ずんだもん「判別プロパティにはunique symbolを保持したまま使いたいね。」
四国めたん「必要に応じて型を狭めたり広げたりしましょう。」
ずんだもん「設計段階でどこまでユニークさを保つか決めるのが大事だよ。」
四国めたん「型の継承関係を押さえておけば混乱しません。」
ずんだもん「symbolファミリーを正しく使い分けよう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: unique symbol は symbol に代入できる */
const UNIQUE = Symbol("unique");
let general: symbol = UNIQUE; // OK

/** Example 2: 逆代入は不可 */
let another: symbol = Symbol("another");
// const keepUnique: typeof UNIQUE = another; // エラー

/** Example 3: ワイドニングの制御 */
function register(id: symbol) {
  console.log(id);
}
register(UNIQUE); // unique symbol が symbol に拡張される
```
