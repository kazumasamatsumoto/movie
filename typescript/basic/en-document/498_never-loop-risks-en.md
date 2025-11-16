# #498 "Risks"

Shikoku Metan: "Infinite loops can hog resources."
Zundamon: "badLoop() burned CPU."
Shikoku Metan: "goodLoop() and asyncLoop() inserted waits."
Zundamon: "Always consider resource impact."

---

## 📺 Code for Display

```typescript
/** Example 1: Bad example */
function badLoop(): never {
  while (true) {
    // CPU 100%
  }
}

/** Example 2: Good example */
function goodLoop(): never {
  while (true) {
    doWork();
    sleep(100);
  }
}

/** Example 3: Async loop */
async function asyncLoop(): never {
  while (true) {
    await processTask();
    await delay(1000);
  }
}
```
