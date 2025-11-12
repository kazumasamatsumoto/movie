# #492 "while(true)"

Shikoku Metan: "Explicit while(true) loops often return never."
Zundamon: "loop() kept calling doWork()."
Shikoku Metan: "poll() polled the queue repeatedly."
Zundamon: "monitor() watched status with delays."
Shikoku Metan: "Insert sleeps/awaits to free the CPU."

---

## 📺 Code for Display

```typescript
/** Example 1: Basic loop */
function loop(): never {
  while (true) {
    doWork();
  }
}

/** Example 2: Polling */
function poll(): never {
  while (true) {
    const data = fetchData();
    if (data) {
      process(data);
    }
    sleep(1000);
  }
}

/** Example 3: Monitoring loop */
async function monitor(): never {
  while (true) {
    const status = checkStatus();
    if (status === "error") {
      handleError();
    }
    await delay(5000);
  }
}
```
