# #801 「unique symbolの型推論」

四国めたん「constでSymbol()を呼ぶと型は自動的にunique symbolになります。」
ずんだもん「typeof IDって書くとそのリテラル型を参照できるんだね。」
四国めたん「はい、letやvarだと一般的なsymbol型に広がります。」
ずんだもん「推論結果を意識しないと意図しない型拡張が起こるよ。」
四国めたん「型エイリアスでunique symbolを包むと共有が楽です。」
ずんだもん「推論ルールを理解して型安全にトークンを扱おう！」
四国めたん「unique symbolの推論はSymbol.forとは異なる点にも注意です。」
ずんだもん「コンパイラの挙動を味方に付けよう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: const推論 */
const ID = Symbol("ID");
// 型: typeof ID (unique symbol)

/** Example 2: letは広がる */
let temp = Symbol("temp");
// 型: symbol

/** Example 3: 型エイリアス */
type IdToken = typeof ID;
function accepts(id: IdToken) {
  return id === ID;
}
```
