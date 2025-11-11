# #312 「無効時の挙動」

四国めたん「strictNullChecks無効時の挙動について学びましょう!」
ずんだもん「無効だとどうなるの?」
四国めたん「はい。全ての型にnullとundefinedが暗黙的に含まれるため、危険なコードを書けてしまいます。」
ずんだもん「string型にnullを代入してtoUpperCase()を呼ぶと実行時エラーなんだね!」
四国めたん「その通りです。コンパイルエラーにならないため、バグに気づきにくいです。」
ずんだもん「関数の引数にnullを渡してもエラーにならないの?」
四国めたん「はい。greet(null)のような呼び出しが可能で、実行時にクラッシュする危険があります。」
ずんだもん「型チェックが不十分だから、strictNullChecksを有効にすべきなのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 実行時エラーの危険 */
// strictNullChecks: false
let name: string = null; // OK
name.toUpperCase(); // 実行時エラー!

/** Example 2: すべての型にnull/undefinedが含まれる */
function greet(name: string) {
  // nameがnullかもしれない
  return name.toUpperCase(); // 危険
}
greet(null); // エラーなし

/** Example 3: 型チェックが不十分 */
interface User {
  name: string;
}
const user: User = { name: null }; // OK
```
