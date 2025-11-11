# #297 「undefinedの宣言」

四国めたん「undefinedの宣言について学びましょう!」
ずんだもん「どうやって宣言するの?」
四国めたん「はい。undefined型やUnion型で宣言できます。」
ずんだもん「name?: stringはオプショナルプロパティだね!」
四国めたん「その通りです。省略可能で、string | undefinedと同じ意味です。」
ずんだもん「関数パラメータでも使える?」
四国めたん「はい。関数パラメータもオプショナルにできます。」
ずんだもん「??演算子でデフォルト値を設定すると便利なのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: undefined型の宣言 */
let value: undefined = undefined;
let name: string | undefined;

/** Example 2: オプショナルプロパティ */
interface User {
  name?: string;  // string | undefined
  age?: number;   // number | undefined
}

/** Example 3: 関数パラメータ */
function greet(name?: string): void {
  console.log(name ?? "Guest");
}
```
