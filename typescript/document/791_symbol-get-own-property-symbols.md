# #791 「Object.getOwnPropertySymbols()」

四国めたん「Object.getOwnPropertySymbolsはシンボルキーだけを配列で返します。」
ずんだもん「隠しプロパティをチェックするのに使えるね。」
四国めたん「文字列キーは含まれません。」
ずんだもん「Reflect.ownKeysとの違いも覚えておこう。」
四国めたん「戻り値はsymbol[]なのでTypeScriptで型安全に扱えます。」
ずんだもん「監査やデバッグで大活躍だよ。」
四国めたん「使い方を確認して管理を楽にしましょう。」
ずんだもん「シンボル管理の第一歩だね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: シンボル一覧 */
const KEY1 = Symbol("k1");
const KEY2 = Symbol("k2");
const target = { [KEY1]: 1, [KEY2]: 2, name: "demo" };
const symbols = Object.getOwnPropertySymbols(target);
console.log(symbols); // [Symbol(k1), Symbol(k2)]

/** Example 2: 値を確認 */
for (const sym of symbols) {
  console.log(sym.description, (target as Record<symbol, unknown>)[sym]);
}

/** Example 3: 監査ヘルパー */
function listSymbols(value: object) {
  return Object.getOwnPropertySymbols(value).map((sym) => sym.description ?? "");
}
console.log(listSymbols(target));
```
