# #735 「symbol型の宣言」

四国めたん「symbol型は型注釈を使って明示的に宣言できます。」
ずんだもん「let key: symbol = Symbol("key");みたいに書けばいいんだね。」
四国めたん「constで宣言すればそのシンボル値が保持されます。」
ずんだもん「DIトークン定義みたいに再利用したいときはconstが便利だよ。」
四国めたん「オブジェクトのプロパティキー型にもsymbol型を指定できます。」
ずんだもん「型レベルで衝突しないことが分かると安心だよね。」
四国めたん「狙いに応じてsymbol型とunique symbolを使い分けましょう。」
ずんだもん「まずは基本の宣言スタイルからしっかり押さえよう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: let宣言 */
let key: symbol = Symbol("cacheKey");
key = Symbol("cacheKey"); // 再代入で新しい値を入れ直せる

/** Example 2: const宣言 */
const TOKEN: symbol = Symbol("token");
const container = { [TOKEN]: "service" };
console.log(container[TOKEN]);

/** Example 3: プロパティキー型の注釈 */
interface Registry {
  [KEY: symbol]: unknown;
}
const registry: Registry = { [Symbol("x")]: 1 };
```
