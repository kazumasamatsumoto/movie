# #496 「サーバープロセス」

四国めたん「サーバープロセスはnever関数の代表です。」
ずんだもん「startHttpServerはrequestを受け続けてた!」
四国めたん「runTcpServerやworkerProcessも例に挙がっていました。」
ずんだもん「待機時にはsleepでCPUを開放する配慮があるね。」
四国めたん「サーバー系ループは終了条件が無いのでneverが適しています。」

---

## 📺 画面表示用コード

```typescript
/** Example 1: HTTPサーバー */
function startHttpServer(port: number): never {
  const server = createServer(port);
  while (true) {
    const request = server.accept();
    handleHttpRequest(request);
  }
}

/** Example 2: TCPサーバー */
function runTcpServer(): never {
  const listener = listen(8080);
  while (true) {
    const socket = listener.accept();
    processConnection(socket);
  }
}

/** Example 3: ワーカープロセス */
function workerProcess(): never {
  console.log("Worker started");
  while (true) {
    const job = fetchJob();
    if (job) {
      executeJob(job);
    } else {
      sleep(1000);
    }
  }
}
```
