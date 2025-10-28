# #1057 「戻り値型 - T | undefined」

四国めたん「findの戻り値型はT | undefinedです。」
ずんだもん「要素が見つからない可能性があるからだね。」
四国めたん「結果を使うときはundefinedチェックが必要です。」
ずんだもん「OptionalチェーンやNullish Coalescingと相性がいいよ。」
四国めたん「戻り値型を理解して安全に扱いましょう。」
ずんだもん「undefinedの扱いを忘れずに！」

---

## 📺 画面表示用コード

```typescript
const users = [
  { id: "u1", active: false },
  { id: "u2", active: true },
];

const found = users.find((user) => user.active);

if (found) {
  console.log(found.id);
}

const name = users.find((user) => user.active)?.id ?? "anonymous";
```
