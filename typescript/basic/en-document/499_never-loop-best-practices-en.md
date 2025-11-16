# #499 "Best Practices"

Shikoku Metan: "Follow best practices when writing infinite loops."
Zundamon: "serverLoop() logged startup."
Shikoku Metan: "safeLoop() wrapped work in try-catch with delays."
Zundamon: "gracefulLoop() exited when a signal flipped the flag."
Shikoku Metan: "Handle errors and graceful shutdowns."

---

## 📺 Code for Display

```typescript
/** Example 1: Logged loop */
function serverLoop(): never {
  console.log("Server started");
  while (true) {
    const request = waitForRequest();
    handleRequest(request);
  }
}

/** Example 2: Error handling */
async function safeLoop(): never {
  while (true) {
    try {
      await processTask();
    } catch (error) {
      console.error("Error:", error);
    }
    await delay(1000);
  }
}

/** Example 3: Shutdown signal */
let shouldRun = true;
function gracefulLoop(): void {
  while (shouldRun) {
    doWork();
  }
  cleanup();
}
process.on('SIGTERM', () => { shouldRun = false; });
```
