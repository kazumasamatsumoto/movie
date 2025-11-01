# #771 「Symbol.hasInstance」

四国めたん「Symbol.hasInstanceはinstanceofの判定ロジックをカスタマイズします。」
ずんだもん「classのstaticメソッドとして実装するんだよね。」
四国めたん「valueを受け取ってbooleanを返します。」
ずんだもん「プロキシや型ブランドに使うと便利そうだよ。」
四国めたん「ただし乱用すると可読性が下がるので用途を限定しましょう。」
ずんだもん「テストで挙動をしっかり検証したいね。」
四国めたん「Symbol.hasInstanceで柔軟なinstanceofを実現できます。」
ずんだもん「特殊な判定が必要なときに覚えておこう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: カスタムinstanceof */
class JsonString {
  static [Symbol.hasInstance](value: unknown): boolean {
    if (typeof value !== "string") return false;
    try {
      JSON.parse(value);
      return true;
    } catch {
      return false;
    }
  }
}

/** Example 2: 使用例 */
console.log('{"a":1}' instanceof JsonString); // true
console.log("plain" instanceof JsonString); // false

/** Example 3: 型ブランドとの併用 */
type BrandedJson = string & { readonly __brand: unique symbol };
function asJsonString(value: string): BrandedJson {
  if (!(value instanceof JsonString)) throw new Error("invalid json");
  return value as BrandedJson;
}
```
