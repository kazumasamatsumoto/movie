# #1036 「チェーン」

四国めたん「filterはmapやreduceとチェーンして使うことが多いです。」
ずんだもん「まずfilterで絞ってからmapで整形、みたいな流れだね。」
四国めたん「型が徐々に変わるので中間の型にも注意しましょう。」
ずんだもん「可読性を保つために適度に改行するといいよ。」
四国めたん「チェーンで型安全なパイプラインを組み立ててください。」
ずんだもん「filterが前段にあると安心だね！」

---

## 📺 画面表示用コード

```typescript
const responses = [
  { status: 200, body: { message: "ok" } },
  { status: 500, body: { message: "error" } },
  { status: 200, body: { message: "done" } },
];

/** Example 1: filter + map */
const messages = responses
  .filter((res) => res.status === 200)
  .map((res) => res.body.message);

/** Example 2: filter + reduce */
const successCount = responses
  .filter((res) => res.status === 200)
  .reduce((acc) => acc + 1, 0);

/** Example 3: 多段チェーン */
const upper = responses
  .filter((res) => res.status === 200)
  .map((res) => res.body.message)
  .map((message) => message.toUpperCase());
```
