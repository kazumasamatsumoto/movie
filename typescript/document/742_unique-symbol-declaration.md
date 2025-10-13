# #742 「unique symbolの宣言」

四国めたん「unique symbolを型注釈に使うにはconstまたはreadonly staticが必要です。」
ずんだもん「ambient宣言でもdeclare const TOKEN: unique symbolみたいに書けるよ。」
四国めたん「クラスのreadonly staticフィールドならunique symbolを外部に公開できます。」
ずんだもん「DIトークンを型として輸出する時に便利だね。」
四国めたん「interfaceではunique symbolをメンバ名として宣言できます。」
ずんだもん「型レベルで同一性を保証できるのが魅力だよ。」
四国めたん「宣言ルールを守ることでコンパイルエラーを防ぎましょう。」
ずんだもん「定義のパターンを押さえておけば運用が楽になるよ！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: ambient宣言 */
declare const HTTP_TOKEN: unique symbol;
export type HttpToken = typeof HTTP_TOKEN;

/** Example 2: クラスのreadonly static */
class Tokens {
  static readonly CONFIG: unique symbol = Symbol("CONFIG");
}
type ConfigToken = typeof Tokens.CONFIG;

/** Example 3: interfaceでのメンバ名 */
interface ExtensionRegistry {
  [HTTP_TOKEN]: string;
}
```
