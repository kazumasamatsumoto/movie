# #316 「null代入エラー」

四国めたん「strictNullChecksでnull代入エラーについて学びましょう!」
ずんだもん「string型にnullを代入するとエラーになるんだね!」
四国めたん「はい。strictNullChecks有効時、nullは明示的に許可が必要です。」
ずんだもん「修正方法1はUnion型で string | null と書くんだよね?」
四国めたん「その通りです。型にnullを含めることで代入が可能になります。」
ずんだもん「Non-Null Assertionも使えるけど、非推奨なの?」
四国めたん「はい。型チェックを回避するため、実行時エラーのリスクがあります。」
ずんだもん「Union型でnullを明示的に扱う方が型安全なのだ!」

---


```typescript
/** Example 1: strictNullChecks有効時のエラー */
// strictNullChecks: true
let name: string = null; // エラー
// Type 'null' is not assignable to type 'string'

/** Example 2: 修正方法1 - Union型 */
let name: string | null = null; // OK
name = "Alice"; // OK

/** Example 3: 修正方法2 - Non-Null Assertion (非推奨) */
let name: string = null!; // OK (型チェック回避)
// 実行時エラーのリスクあり
```
