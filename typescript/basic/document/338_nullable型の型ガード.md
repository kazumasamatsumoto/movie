# #338 「nullable型の型ガード」

四国めたん「nullable型の型ガードについて学びましょう!」
ずんだもん「型ガード関数でnullを判定できるんだね!」
四国めたん「はい。isNotNull関数で、値がnullでないことを型レベルで保証できます。」
ずんだもん「value is T っていう書き方が重要なの?」
四国めたん「その通りです。これで、TypeScriptが型を自動的に絞り込んでくれます。」
ずんだもん「配列のfilterと組み合わせられるんだね!」
四国めたん「はい。nullを含む配列から、nullを除外した配列を安全に作れます。」
ずんだもん「型ガードで、型安全なコードが書けるのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 型ガード関数 */
function isNotNull<T>(value: T | null): value is T {
  return value !== null;
}

/** Example 2: 使用例 */
const user: User | null = getUser();
if (isNotNull(user)) {
  user.name; // User型として扱える
}

/** Example 3: 配列のfilterと組み合わせ */
const users: (User | null)[] = [user1, null, user2];
const validUsers: User[] = users.filter(isNotNull);
```
