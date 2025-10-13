# #750 「基本まとめ」

四国めたん「symbol型の基本をまとめましょう。」
ずんだもん「一意なプリミティブで、説明文が同じでも値が違うんだったね。」
四国めたん「プロパティキーに使うと列挙から除外できます。」
ずんだもん「unique symbolはconst宣言で得られるリテラル型だったよ。」
四国めたん「typeofや型階層を理解すると推論が見えてきます。」
ずんだもん「基本パターンを覚えてフレームワーク開発にも活かしたいね。」
四国めたん「次はSymbol.forで共有パターンを学びましょう。」
ずんだもん「さらに深くsymbolを掘り下げるよ！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: symbol生成 */
const token = Symbol("token");

/** Example 2: プロパティキー */
const obj = { [token]: "value" };
console.log(Object.keys(obj)); // []

/** Example 3: unique symbolの型 */
const FLAG = Symbol("FLAG");
type Flag = typeof FLAG;
const useFlag = (flag: Flag) => flag === FLAG;
```
