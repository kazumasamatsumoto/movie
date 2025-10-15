# #1088 「実践例」

四国めたん「実践例として、禁止ワードチェックを実装してみましょう。」
ずんだもん「入力テキストを分割して、禁止ワードリストに含まれているか調べるんだね。」
四国めたん「はい、someとincludesを組み合わせると簡潔に書けます。」
ずんだもん「ユーザー投稿の検証で役立つよ。」
四国めたん「実例を参考に存在チェックを組み立ててください。」
ずんだもん「コンテンツを安全に保とう！」

---

## 📺 画面表示用コード

```typescript
const bannedWords = ["spam", "ban"];

function containsBannedWord(message: string) {
  return message.split(/\s+/).some((word) => bannedWords.includes(word.toLowerCase()))
}

const comment = "This is Spam content";
const hasBanned = containsBannedWord(comment);
```
