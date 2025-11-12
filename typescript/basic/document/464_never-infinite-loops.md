# #464 「無限ループ」

四国めたん「無限ループを作る関数もneverです。」
ずんだもん「runForeverがwhile(true)でログを出してた!」
四国めたん「startServerのようなメインループも終了しません。」
ずんだもん「イベントループも同じで、常に次のイベントを処理するんだね。」
四国めたん「neverを付けると制御が戻らないことが明確になります。」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 無限ループ */
function runForever(): never {
  while (true) {
    console.log("Running...");
  }
}

/** Example 2: サーバーメインループ */
function startServer(): never {
  while (true) {
    const request = waitForRequest();
    handleRequest(request);
  }
}

/** Example 3: イベントループ */
function eventLoop(): never {
  while (true) {
    const event = getNextEvent();
    processEvent(event);
  }
}
```
