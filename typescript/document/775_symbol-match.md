# #775 「Symbol.match」

四国めたん「Symbol.matchはString.prototype.matchの挙動をオーバーライドします。」
ずんだもん「RegExp以外のオブジェクトでもマッチ処理を提供できるんだね。」
四国めたん「戻り値は通常のmatch結果と同じ配列かnullです。」
ずんだもん「バリデータをラップするのに便利そうだよ。」
四国めたん「TypeScriptでは(value: string) => RegExpMatchArray | nullという型になります。」
ずんだもん「Symbol.matchで高度なパターンマッチを作ろう！」
四国めたん「副作用なく設計するのがポイントです。」
ずんだもん「拡張正規表現みたいに使えて楽しいね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: カスタムマッチャー */
const startsWithHash = {
  [Symbol.match](text: string): RegExpMatchArray | null {
    if (text.startsWith("#")) {
      return [text];
    }
    return null;
  },
};

/** Example 2: String.prototype.matchで使用 */
console.log("#tag".match(startsWithHash)); // ["#tag"]
console.log("tag".match(startsWithHash)); // null

/** Example 3: 型推論 */
function isHashTag(value: string) {
  return value.match(startsWithHash) !== null;
}
console.log(isHashTag("#ts"));
```
