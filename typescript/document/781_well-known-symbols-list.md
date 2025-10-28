# #781 「一覧」

四国めたん「Well-known Symbolsにはiterator、asyncIterator、toStringTagなどが含まれます。」
ずんだもん「Symbolオブジェクトの静的プロパティとしてアクセスできるんだね。」
四国めたん「Reflect.ownKeys(Symbol)で一覧も取得できます。」
ずんだもん「仕様書に載っているものはほぼTypeScriptのlibでも定義済みだよ。」
四国めたん「一覧を把握しておくと必要なときにすぐ使えます。」
ずんだもん「リファレンスを手元に置いておくと便利だね。」
四国めたん「各シンボルの役割を簡単に振り返りましょう。」
ずんだもん「次の実践例で実際に使ってみるよ！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: Symbolのキー一覧 */
const keys = Reflect.ownKeys(Symbol).filter((key) => typeof key === "string");
console.log(keys);

/** Example 2: 存在確認 */
console.log("iterator" in Symbol); // true
console.log("matchAll" in Symbol); // true (ES2020)

/** Example 3: 型の参照 */
type WellKnown = typeof Symbol.iterator | typeof Symbol.toPrimitive;
const iterKey: WellKnown = Symbol.iterator;
```
