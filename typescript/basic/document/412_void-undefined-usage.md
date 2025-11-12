# #412 「使い分け」

四国めたん「voidとundefinedの使い分けを確認しましょう。」
ずんだもん「saveDataは副作用だけだからvoidだね。」
四国めたん「はい。戻り値を気にしない処理です。」
ずんだもん「loadDataはData | undefinedを返して検索結果を表すんだ?」
四国めたん「その通り。値が見つからないケースを伝えます。」
ずんだもん「UserServiceでもgetUserとdeleteUserの戻り値が違う!」
四国めたん「検索系はundefined、更新系はvoidにすると読みやすいです。」
ずんだもん「役割に応じて型を選ぶのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: void: 副作用 */
function saveData(data: Data): void {
  database.save(data);
}

/** Example 2: undefined: 値を返す */
function loadData(id: number): Data | undefined {
  return database.find(id);
}

/** Example 3: 実践的な使い分け */
interface UserService {
  getUser(id: number): User | undefined;
  deleteUser(id: number): void;
  saveUser(user: User): void;
}
```
