# #411 「undefined戻り値使用」

四国めたん「undefinedを返す関数は値として扱えることを覚えましょう。」
ずんだもん「findUserはUser | undefinedを返していたね。」
四国めたん「はい。戻り値を変数に受け取ってチェックします。」
ずんだもん「user !== undefined ならUser型として扱えるんだ?」
四国めたん「その通り。条件分岐で安全にプロパティを参照できます。」
ずんだもん「Optional Chainingと??を組み合わせるパターンも便利!」
四国めたん「name = findUser(2)?.name ?? "Unknown" のように書けます。」
ずんだもん「undefined戻り値を値として扱うコツを身につけるのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: undefined戻り値 */
function findUser(id: number): User | undefined {
  return users.find(u => u.id === id);
}
const user = findUser(1);

/** Example 2: 値としてチェック */
if (user !== undefined) {
  console.log(user.name);
}

/** Example 3: Optional Chaining */
const name = findUser(2)?.name ?? "Unknown";
const email = findUser(3)?.email;
```
