# #1075 「戻り値型 - boolean」

四国めたん「everyも戻り値はbooleanです。」
ずんだもん「全部OKならtrue、一つでもNGならfalseになるんだね。」
四国めたん「はい、早期終了するので効率的です。」
ずんだん「someと組み合わせて条件分岐を書くと読みやすいよ。」
四国めたん「戻り値型を活かしてロジックを組み立ててください。」
ずんだん「boolean操作にぴったりだね！」

---

## 📺 画面表示用コード

```typescript
const tasks = [
  { title: "Design", done: true },
  { title: "Implement", done: false },
];

const allDone = tasks.every((task) => task.done); // false

if (!allDone) {
  console.log("There are remaining tasks");
}
```
