# #494 "Use Cases"

Shikoku Metan: "Real systems often rely on infinite loops."
Zundamon: "We saw WebSocket servers and queue processors."
Shikoku Metan: "watchFiles kept detecting file changes."
Zundamon: "Insert delay() to control polling intervals."
Shikoku Metan: "Follow these examples to avoid runaway loops."

---

## 📺 Code for Display

```typescript
/** Example 1: WebSocket server */
function runWebSocketServer(): never {
  const server = createServer();
  while (true) {
    const connection = server.accept();
    handleConnection(connection);
  }
}

/** Example 2: Task queue */
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

/** Example 3: Watcher */
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
