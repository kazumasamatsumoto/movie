# #337 「関数戻り値のnullable」

四国めたん「関数戻り値のnullableについて学びましょう!」
ずんだもん「関数の戻り値をnullable型にできるんだね!」
四国めたん「はい。User | null を返すことで、見つからない場合をnullで表現できます。」
ずんだもん「呼び出し側でnullチェックが必要になるの?」
四国めたん「その通りです。if (user !== null) で、nullでない場合の処理を書きます。」
ずんだもん「Nullish Coalescingも使えるんだね!」
四国めたん「はい。?? 演算子で、nullの場合のデフォルト処理を簡潔に書けます。」
ずんだもん「nullable戻り値で、安全な関数設計ができるのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: nullable戻り値 */
function findUser(id: number): User | null {
  const user = users.find(u => u.id === id);
  return user ?? null;
}

/** Example 2: 呼び出し側の処理 */
const user = findUser(1);
if (user !== null) {
  console.log(user.name);
}

/** Example 3: Nullish Coalescingで簡潔に */
const user = findUser(1) ?? createGuestUser();
const name = findUser(1)?.name ?? "Unknown";
```
