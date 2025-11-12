# #464 "Infinite Loops"

Shikoku Metan: "Functions containing infinite loops are never."
Zundamon: "runForever printed continuously."
Shikoku Metan: "startServer is another endless loop."
Zundamon: "eventLoop keeps fetching events forever."
Shikoku Metan: "Annotate them with never to show control never returns."

---

## 📺 Code for Display

```typescript
/** Example 1: Infinite loop */
function runForever(): never {
  while (true) {
    console.log("Running...");
  }
}

/** Example 2: Server main loop */
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
    processEvent(event);
  }
}
```
