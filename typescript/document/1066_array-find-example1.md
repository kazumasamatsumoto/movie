# #1066 「実践例(1)」

四国めたん「実践例として、ユーザー一覧から指定IDのユーザーを探しましょう。」
ずんだもん「findでマッチしたユーザーを取得するんだね。」
四国めたん「はい、結果がundefinedの場合のフォールバックも合わせて書きます。」
ずんだもん「OptionalチェーンやNullish Coalescingが活躍するよ。」
四国めたん「実例でfindの挙動を確認してください。」
ずんだもん「検索処理にすぐ使えるね！」

---

## 📺 画面表示用コード

```typescript
interface User {
  id: string;
  name: string;
}

const users: User[] = [
  { id: "u1", name: "meta" },
  { id: "u2", name: "zunda" },
];

const targetId = "u2";

const found = users.find((user) => user.id === targetId);

const displayName = found?.name ?? "anonymous";
```
