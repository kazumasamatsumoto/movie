# #1061 「findIndex()の戻り値」

四国めたん「findIndexの戻り値はnumber型で、見つからなければ-1です。」
ずんだもん「-1チェックを忘れるとバグになるんだね。」
四国めたん「はい、結果をインデックスアクセスに使う前に必ず確認しましょう。」
ずんだもん「Nullish Coalescingでフォールバックするのもアリだよ。」
四国めたん「戻り値の扱い方を覚えておきましょう。」
ずんだもん「安全にインデックスを使ってね！」

---

## 📺 画面表示用コード

```typescript
const users = ["meta", "zunda"];

const index = users.findIndex((user) => user === "zunda");

if (index !== -1) {
  console.log(users[index]);
} else {
  console.log("not found");
}

const fallback = users[users.findIndex((user) => user === "unknown")] ?? "anonymous";
```
