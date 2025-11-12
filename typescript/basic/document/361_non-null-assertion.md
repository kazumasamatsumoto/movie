# #361 「Non-null Assertionとは - !」

四国めたん「Non-null Assertion演算子(!)でnullを無視して扱う方法を紹介します!」
ずんだもん「document.getElementById("app")! のように末尾に!を付けるだけなんだね?」
四国めたん「はい。要素が必ず存在すると分かっているならHTMLElementとして扱えます。」
ずんだもん「User | null の戻り値にも使えるの?」
四国めたん「getUser()! と書けばUser型としてプロパティにアクセスできます。」
ずんだもん「string | undefined のvalueにも効く?」
四国めたん「value!.length のように書けばundefinedを取り除いたstringとして評価されます。」
ずんだもん「使い所を見極めてNon-null Assertionを活用するのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: DOM要素を強制的に扱う */
const element = document.getElementById("app")!;
// HTMLElement型として扱える(null可能性を無視)
element.innerHTML = "Hello";

/** Example 2: nullable戻り値に適用 */
function getUser(): User | null {
  return { name: "Alice", age: 30 };
}
const user = getUser()!;  // User型として扱う
console.log(user.name);

/** Example 3: undefinedable値に適用 */
let value: string | undefined = "hello";
const length = value!.length;  // stringとして扱う
```
