# #500 "Infinite Loop Summary"

Shikoku Metan: "Let's summarize infinite loop tips."
Zundamon: "eventLoop covers the basics."
Shikoku Metan: "Add delays to free CPU."
Zundamon: "safeLoop reminded us to handle errors."
Shikoku Metan: "Follow these to keep loops stable."

---

## 📺 Code for Display

```typescript
/** Example 1: Basic loop */
function eventLoop(): never {
  while (true) {
    const event = getEvent();
    processEvent(event);
  }
}

/** Example 2: Proper waiting */
async function serverLoop(): never {
  while (true) {
    const request = await waitForRequest();
    await handleRequest(request);
    await delay(100);
  }
}

/** Example 3: Error handling */
function safeLoop(): never {
  while (true) {
    try {
      processTask();
    } catch (error) {
      console.error(error);
    }
  }
}
```
