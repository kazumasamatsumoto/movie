# #1073 「使用例」

四国めたん「someの使用例として、バリデーションを考えてみましょう。」
ずんだもん「禁止タグが含まれていないかチェックするみたいなケースだね。」
四国めたん「はい、条件に一致したらアラートを出す処理を組みます。」
ずんだん「短絡評価のおかげで効率的に判定できるよ。」
四国めたん「使用例でイメージを掴んでください。」
ずんだん「バリデーションにぴったりだね！」

---

## 📺 画面表示用コード

```typescript
const tags = ["typescript", "es2023", "deprecated"];
const banned = ["deprecated", "legacy"];

const hasBannedTag = tags.some((tag) => banned.includes(tag));

if (hasBannedTag) {
  console.warn("banned tag found");
}
```
