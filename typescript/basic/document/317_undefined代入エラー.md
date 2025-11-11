# #317 「undefined代入エラー」

四国めたん「strictNullChecksでundefined代入エラーについて学びましょう!」
ずんだもん「string型にundefinedを代入するとエラーになるんだね!」
四国めたん「はい。strictNullChecks有効時、undefinedも明示的に許可が必要です。」
ずんだもん「修正方法1はUnion型で string | undefined と書くんだよね?」
四国めたん「その通りです。型にundefinedを含めることで代入が可能になります。」
ずんだもん「修正方法2のオプショナルも便利そうだね!」
四国めたん「はい。プロパティや引数に?を付けると string | undefined になります。」
ずんだもん「型でundefinedを明示的に扱う方が安全なのだ!」

---


```typescript
/** Example 1: strictNullChecks有効時のエラー */
// strictNullChecks: true
let name: string = undefined; // エラー
// Type 'undefined' is not assignable to type 'string'

/** Example 2: 修正方法1 - Union型 */
let name: string | undefined = undefined; // OK
name = "Alice"; // OK

/** Example 3: 修正方法2 - オプショナル */
interface User {
  name?: string; // string | undefined
}
function greet(name?: string) {}
```
