# #333 「nullable配列」

四国めたん「nullable配列について学びましょう!」
ずんだもん「配列の要素がnullableな場合の処理なんだね!」
四国めたん「はい。(User | null)[] で、配列の各要素がUserかnullになります。」
ずんだもん「nullを除外するにはどうするの?」
四国めたん「その通りです。filterとisNotNull型ガード関数を使って、nullでない要素だけを取り出せます。」
ずんだもん「mapで処理する時も注意が必要だね!」
四国めたん「はい。map(u => u?.name ?? "Unknown") のように、Optional Chainingを使って安全に処理できます。」
ずんだもん「nullable配列を適切に扱って、安全なコードを書くのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: nullable要素の配列 */
const users: (User | null)[] = [user1, null, user2];
const names = users.filter(u => u !== null);

/** Example 2: 型ガードでフィルタ */
function isNotNull<T>(value: T | null): value is T {
  return value !== null;
}
const validUsers = users.filter(isNotNull);

/** Example 3: map処理 */
const userNames = users.map(u => u?.name ?? "Unknown");
```
