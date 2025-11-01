# #746 「特性」

四国めたん「symbolは文字列へ暗黙変換されません。」
ずんだもん「+演算子やtemplate literalに混ぜるとTypeErrorになるんだよね。」
四国めたん「列挙対象から外れる性質も特徴です。」
ずんだもん「descriptionプロパティで人間向けのラベルが確認できるよ。」
四国めたん「また、真偽値評価では常にtrueです。」
ずんだもん「シンボル専用のAPIだけを使うのが安全だね。」
四国めたん「特性を理解して誤用を避けましょう。」
ずんだもん「TypeScriptが補完してくれるけど基本を押さえておこう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 文字列との連結は不可 */
const sym = Symbol("id");
// console.log("user:" + sym); // TypeError
console.log(sym.toString()); // 明示変換は可能

/** Example 2: 真偽値評価 */
if (sym) {
  console.log("symbolはtruthy");
}

/** Example 3: description */
console.log(sym.description); // "id"
```
