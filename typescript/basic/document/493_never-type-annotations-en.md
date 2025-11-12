# #493 "Type Annotations"

Shikoku Metan: "Annotate infinite loops with never."
Zundamon: "startServer(): never documents the intent."
Shikoku Metan: "Tiny helpers may rely on inference."
Zundamon: "Public APIs like runEventLoop() should be explicit?"
Shikoku Metan: "Yes—callers must know it never returns."

---

## 📺 Code for Display

```typescript
/** Example 1: Explicit annotation */
function startServer(): never {
  while (true) {
    handleRequest();
  }
}

/** Example 2: Rely on inference */
function loop() {
  while (true) {
    doWork();
  }
}

/** Example 3: Public API */
export function runEventLoop(): never {
  while (true) {
    const event = getEvent();
    processEvent(event);
  }
}
```
