# #496 "Server Processes"

Shikoku Metan: "Server processes are classic never functions."
Zundamon: "startHttpServer kept accepting requests."
Shikoku Metan: "runTcpServer and workerProcess were other examples."
Zundamon: "Notice the sleep when no job is available."
Shikoku Metan: "Since servers never stop, annotate them with never."

---

## 📺 Code for Display

```typescript
/** Example 1: HTTP server */
function startHttpServer(port: number): never {
  const server = createServer(port);
  while (true) {
    const request = server.accept();
    handleHttpRequest(request);
  }
}

/** Example 2: TCP server */
function runTcpServer(): never {
  const listener = listen(8080);
  while (true) {
    const socket = listener.accept();
    processConnection(socket);
  }
}

/** Example 3: Worker process */
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
