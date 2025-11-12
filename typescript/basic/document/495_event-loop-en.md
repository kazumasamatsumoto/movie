# #495 "Event Loop"

Shikoku Metan: "Event loops exemplify never functions."
Zundamon: "eventLoop() waited for events and dispatched them."
Shikoku Metan: "mainLoop batched events via pollEvents()."
Zundamon: "priorityLoop handled highest-priority tasks first."
Shikoku Metan: "Tailor the loop to your design needs."

---

## 📺 Code for Display

```typescript
/** Example 1: Basic loop */
function eventLoop(): never {
  while (true) {
    const event = waitForEvent();
    dispatchEvent(event);
  }
}

/** Example 2: Multiple sources */
function mainLoop(): never {
  while (true) {
    const events = pollEvents();
    for (const event of events) {
      handleEvent(event);
    }
  }
}

/** Example 3: Priority loop */
function priorityLoop(): never {
  while (true) {
    const event = getHighestPriorityEvent();
    if (event) {
      processEvent(event);
    } else {
      idle();
    }
  }
}
```
