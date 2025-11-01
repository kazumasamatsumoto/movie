# #740 「型推論」

四国めたん「TypeScriptはSymbol()の戻り値をコンテキストに応じて推論します。」
ずんだもん「constだとunique symbol、letだとsymbolになるんだよね。」
四国めたん「再代入できるかどうかで型が変わります。」
ずんだもん「関数の戻り値もsymbol型として推論されるよ。」
四国めたん「必要なら型注釈やas constで狙いを固定しましょう。」
ずんだもん「推論結果を理解してコンパイラを味方にしよう！」
四国めたん「unique symbolは後の章で詳しく扱います。」
ずんだもん「まずは推論ルールを押さえてね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: const推論はunique symbol */
const SERVICE_TOKEN = Symbol("service");
// 型: typeof SERVICE_TOKEN (unique symbol)

/** Example 2: let推論はsymbol */
let currentToken = Symbol("dynamic");
// 型: symbol
currentToken = Symbol("dynamic");

/** Example 3: 関数戻り値推論 */
function createToken(description: string) {
  return Symbol(description);
}
const tokenFromFactory = createToken("factory"); // 型: symbol
```
