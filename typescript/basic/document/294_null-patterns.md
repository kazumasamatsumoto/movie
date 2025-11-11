# #294 「nullのパターン」

四国めたん「nullを使ったデザインパターンについて学びましょう!」
ずんだもん「どんなパターンがあるの?」
四国めたん「はい。Repository、Option型、Null Objectパターンなどがあります。」
ずんだもん「Repositoryパターンはfind系メソッドでnullを返すんだね!」
四国めたん「その通りです。見つからない場合にnullを返します。」
ずんだもん「Option型はT | nullで安全性を高めるの?」
四国めたん「はい。nullを明示的に扱うことで、エラーを防ぎます。」
ずんだもん「Null Objectパターンで??を使ってデフォルト値を設定するのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: Repository パターン */
class UserRepository {
  findById(id: number): User | null {
    return this.users.find(u => u.id === id) ?? null;
  }
}

/** Example 2: Option型パターン */
type Option<T> = T | null;
function safeDivide(a: number, b: number): Option<number> {
  return b !== 0 ? a / b : null;
}

/** Example 3: Null Objectパターン */
const user = findUser(id) ?? createGuestUser();
if (user !== null) {
  console.log(user.name);
}
```
