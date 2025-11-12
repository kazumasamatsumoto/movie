# #493 「型注釈」

四国めたん「無限ループ関数にはnever型注釈を付けましょう。」
ずんだもん「startServer(): never と書くと意図が明確だね。」
四国めたん「小さなヘルパーでは型推論に任せても構いません。」
ずんだもん「公開API runEventLoop() では必ず明示すべき?」
四国めたん「はい。利用者に『戻らない』と伝わります。」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 明示的な注釈 */
function startServer(): never {
  while (true) {
    handleRequest();
  }
}

/** Example 2: 推論に任せる */
function loop() {
  while (true) {
    doWork();
  }
}

/** Example 3: 公開API */
export function runEventLoop(): never {
  while (true) {
    const event = getEvent();
    processEvent(event);
  }
}
```
