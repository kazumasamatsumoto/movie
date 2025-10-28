# #794 「シンボルプロパティのコピー」

四国めたん「Object.assignやスプレッド構文はenumerableなsymbolプロパティもコピーします。」
ずんだもん「列挙されないと思っているとハマるポイントだね。」
四国めたん「非enumerableならコピーされません。」
ずんだもん「Reflect.ownKeysで手動コピーする方法もあるよ。」
四国めたん「コピー戦略を決めてメタデータの漏れを防ぎましょう。」
ずんだもん「テストで意図どおりコピーされるか確認したいね。」
四国めたん「シンボルプロパティの扱いに注意して設計してください。」
ずんだもん「安全なコピー方法を身につけよう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: Object.assign */
const META = Symbol("meta");
const source = { id: 1, [META]: "hidden" };
const clone = Object.assign({}, source);
console.log(clone[META]); // "hidden"

/** Example 2: スプレッド */
const spreadClone = { ...source };
console.log(spreadClone[META]);

/** Example 3: Reflect.ownKeysで制御 */
function copySymbolProps(target: object, sourceObj: object) {
  for (const key of Reflect.ownKeys(sourceObj)) {
    if (typeof key === "symbol") {
      Object.defineProperty(target, key, Object.getOwnPropertyDescriptor(sourceObj, key)!);
    }
  }
}
const manual: Record<symbol, unknown> = {};
copySymbolProps(manual, source);
console.log(manual[META]);
```
