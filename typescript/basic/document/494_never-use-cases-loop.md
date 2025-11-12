# #494 「使用例」

四国めたん「無限ループは現実のシステムでもよくあります。」
ずんだもん「WebSocketサーバーやタスクキューを回し続けていたね。」
四国めたん「watchFilesのようにファイル監視を永続化することもあります。」
ずんだもん「await delayを入れてポーリング間隔を調整するのがコツだ!」
四国めたん「実例を参考にして制御不能なループを避けましょう。」

---

## 📺 画面表示用コード

```typescript
/** Example 1: WebSocketサーバー */
function runWebSocketServer(): never {
  const server = createServer();
  while (true) {
    const connection = server.accept();
    handleConnection(connection);
  }
}

/** Example 2: タスクキュー */
function processQueue(): never {
  while (true) {
    const task = queue.dequeue();
    if (task) {
      executeTask(task);
    } else {
      sleep(100);
    }
  }
}

/** Example 3: 監視プロセス */
async function watchFiles(): never {
  while (true) {
    const changes = detectChanges();
    if (changes.length > 0) {
      handleChanges(changes);
    }
    await delay(1000);
  }
}
```
