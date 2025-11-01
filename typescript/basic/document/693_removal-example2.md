# #693 「any排除実例②」

四国めたん「二つ目の例はフロントエンドのイベントハンドラです」
ずんだもん「message: anyをMessageEvent<unknown>にして型ガードを追加したんだよね」
四国めたん「はい。postMessageとの通信が安全になりバグが激減しました」
ずんだもん「テストも型に沿って書けるからメンテナンスが楽になったよ」
四国めたん「ブラウザAPIでもunknownを活用すると効果的です」
ずんだもん「UIでもanyを残さない方針にしよう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 変更前 */
window.addEventListener("message", (event: any) => {
  console.log(event.data.payload.id);
});

/** Example 2: 変更後 */
window.addEventListener("message", (event: MessageEvent<unknown>) => {
  if (typeof event.data === "object" && event.data !== null && "payload" in event.data) {
    console.log((event.data as { payload: { id: string } }).payload.id);
  }
});

/** Example 3: 型ガード */
const isPayload = (value: unknown): value is { payload: { id: string } } =>
  typeof value === "object" && value !== null && "payload" in value;
```
