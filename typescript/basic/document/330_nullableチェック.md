# #330 「nullableチェック」

四国めたん「nullableチェックについて学びましょう!」
ずんだもん「厳密等価演算子でnullをチェックできるんだね!」
四国めたん「はい。if (user === null) で、nullかどうかを判定できます。」
ずんだもん「型ガード関数も使えるんだよね?」
四国めたん「その通りです。isNotNull関数で、nullでない場合の型を絞り込めます。」
ずんだもん「Nullish Coalescing演算子も便利だね!」
四国めたん「はい。?? を使って、nullの場合のデフォルト値を簡潔に指定できます。」
ずんだもん「適切なnullチェックで、安全なコードを書くのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 厳密等価演算子 */
if (user === null) {
  return "No user";
}
console.log(user.name); // User型

/** Example 2: 型ガード */
function isNotNull<T>(value: T | null): value is T {
  return value !== null;
}
if (isNotNull(user)) {
  user.name; // T型
}

/** Example 3: Nullish Coalescing */
const name = user ?? createGuestUser();
const port = config ?? 3000;
```
