# #340 「nullable型まとめ」

四国めたん「nullable型のまとめをしましょう!」
ずんだもん「Nullable<T> 型で、nullを許容する型を作れるんだね!」
四国めたん「はい。T | null を使って、値の不在を明示的に表現できます。」
ずんだもん「安全なアクセス方法がいくつかあるの?」
四国めたん「その通りです。Optional Chainingや、厳密等価演算子でのnullチェックが使えます。」
ずんだもん「実践パターンでは、filterと組み合わせるんだね!」
四国めたん「はい。isNotNull関数でnullを除外し、安全な配列を作れます。」
ずんだもん「nullable型をマスターして、堅牢なコードを書くのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: nullable型の基本 */
type Nullable<T> = T | null;
function findUser(id: number): Nullable<User> {
  return users.find(u => u.id === id) ?? null;
}

/** Example 2: 安全なアクセス */
const user = findUser(1);
const name = user?.name ?? "Guest";
if (user !== null) {
  console.log(user.email);
}

/** Example 3: 実践パターン */
const users = getUsers();
const validUsers = users.filter(isNotNull);
const names = validUsers.map(u => u.name);
```
