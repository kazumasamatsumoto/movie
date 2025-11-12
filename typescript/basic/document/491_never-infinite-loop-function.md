# #491 「無限ループ関数」

四国めたん「never型は無限ループ関数でも使います。」
ずんだもん「runForever()はprocessTaskを回し続けてたね。」
四国めたん「startServerのようにリクエストを待ち続ける処理もneverになります。」
ずんだもん「eventLoopもイベントを処理し続けるんだ。」
四国めたん「戻り値がないどころか制御が戻らないことを型で示すのがポイントです。」

---

## 📺 画面表示用コード

```typescript
/** Example 1: runForever */
function runForever(): never {
  while (true) {
    console.log("Running...");
    processTask();
  }
}

/** Example 2: サーバーループ */
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
    if (event) {
      processEvent(event);
    }
  }
}
```
