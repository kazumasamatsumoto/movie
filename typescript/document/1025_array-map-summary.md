# #1025 「mapまとめ」

四国めたん「mapのポイントをまとめましょう。」
ずんだもん「コールバックで型変換、戻り値は新しい配列、長さは変わらない、と学んだね。」
四国めたん「はい、型推論や型注釈、型述語との組み合わせも確認しました。」
ずんだもん「チェーンや実践例で使いどころも見えたよ。」
四国めたん「次はfilterのメソッドを詳しく見ていきます。」
ずんだもん「mapを使いこなしてデータ変換を楽しもう！」

---

## 📺 画面表示用コード

```typescript
const numbers = [1, 2, 3];

/** Example 1: 基本変換 */
const doubled = numbers.map((value) => value * 2);

/** Example 2: プロパティ抽出 */
const users = [
  { id: "u1", name: "meta" },
  { id: "u2", name: "zunda" },
];
const usernames = users.map((user) => user.name);

/** Example 3: チェーン */
const summary = numbers.map((value) => value * 2).reduce((acc, cur) => acc + cur, 0);
```
