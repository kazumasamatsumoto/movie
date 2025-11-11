# #329 「nullの代入」

四国めたん「nullの代入について学びましょう!」
ずんだもん「nullable型にはnullを代入できるんだね!」
四国めたん「はい。User | null 型の変数には、いつでもnullを代入できます。」
ずんだもん「初期値としてnullを使うことも多いよね?」
四国めたん「その通りです。まだ値がない状態を明示的に表現できます。」
ずんだもん「ログアウト時にnullで値をリセットするんだね!」
四国めたん「はい。currentUser = null で、ユーザー情報をクリアできます。」
ずんだもん「nullの代入で、状態管理が明確になるのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: null代入 */
let user: User | null = getUser();
user = null; // OK

/** Example 2: 初期値としてのnull */
let cache: Cache | null = null;
function init() {
  cache = new Cache();
}

/** Example 3: リセット時のnull */
let currentUser: User | null = loginUser;
function logout() {
  currentUser = null;
}
```
