# #731 「symbol型とは」

四国めたん「symbol型について学びましょう！」
ずんだもん「シンボルって文字列キーとは何が違うの？」
四国めたん「一意な識別子を生成するためのプリミティブで、同じ説明文でも値が重複しません。」
ずんだもん「つまり名前が衝突しないプロパティキーを作れるんだね。」
四国めたん「オブジェクトの内部メタデータを隠す用途にも使われます。」
ずんだもん「AngularやNest.jsでもフレームワーク側の識別子に活用できそうだよ。」
四国めたん「暗黙的に文字列へ変換されない点が安全性を高めます。」
ずんだもん「ユニークなキーで拡張しやすくなるのが魅力だよ！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: symbolの生成 */
const token = Symbol("serviceToken");
const anotherToken = Symbol("serviceToken");
console.log(token === anotherToken); // false: 説明文が同じでも別値

/** Example 2: 衝突しないプロパティキー */
const registry = {
  [token]: { url: "/api" },
};
registry[token]; // { url: "/api" }

/** Example 3: 文字列へ暗黙変換されない */
const label = Symbol("label");
// String(label); // 実行時エラー: Symbol値を文字列化できない
console.log(label.toString()); // "Symbol(label)"
```
