# #491 "Infinite Loop Functions"

Shikoku Metan: "never also annotates infinite loop functions."
Zundamon: "runForever() kept calling processTask."
Shikoku Metan: "startServer waits for requests forever."
Zundamon: "eventLoop handles events endlessly."
Shikoku Metan: "Use never whenever control never returns."

---

## 📺 Code for Display

```typescript
/** Example 1: runForever */
function runForever(): never {
  while (true) {
    console.log("Running...");
    processTask();
  }
}

/** Example 2: Server loop */
function startServer(): never {
  while (true) {
    const request = waitForRequest();
    handleRequest(request);
  }
}

/** Example 3: Event loop */
function eventLoop(): never {
  while (true) {
    const event = getNextEvent();
    if (event) {
      processEvent(event);
    }
  }
}
```
