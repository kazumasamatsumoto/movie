# #1022 「実践例(1) - データ変換」

四国めたん「mapを使ったデータ変換の実例を見ましょう。」
ずんだもん「APIから受け取った生データをビュー用に整形するケースがいいね。」
四国めたん「はい、数値を文字列にしたり、追加情報を付与したオブジェクトに変換します。」
ずんだもん「mapで整形ロジックを一箇所にまとめられるよ。」
四国めたん「実践例を参考にmapを活用してみてください。」
ずんだもん「変換処理が読みやすくなるよ！」

---

## 📺 画面表示用コード

```typescript
interface UserResponse {
  id: number;
  name: string;
  lastLogin: string;
}

const response: UserResponse[] = [
  { id: 1, name: "meta", lastLogin: "2024-03-01T10:00:00Z" },
  { id: 2, name: "zunda", lastLogin: "2024-03-05T12:30:00Z" },
];

/** Example 1: ビューモデル化 */ 
const viewModels = response.map((user) => ({
  id: `user-${user.id}`,
  displayName: user.name.toUpperCase(),
  lastLogin: new Date(user.lastLogin).toLocaleString(),
}));

/** Example 2: タイムスタンプ抽出 */
const lastLoginTimes = response.map((user) => new Date(user.lastLogin).getTime());

/** Example 3: IDのみ */
const ids = response.map((user) => user.id);
```
