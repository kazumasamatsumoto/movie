# #415 "Comparison Summary"

Shikoku Metan: "Let's summarize the contrast between void and undefined."
Zundamon: "logMessage and the Logger type show pure side effects."
Shikoku Metan: "Yes, findItem exemplifies returning undefined."
Zundamon: "Both console.log outputs show undefined, yet meanings differ?"
Shikoku Metan: "Exactly—void signals 'ignore this', undefined means 'no data'."
Zundamon: "So intent is everything."
Shikoku Metan: "Use this summary to pick the right type quickly."
Zundamon: "I'll keep those comparison points handy!"

---

## 📺 Code for Display

```typescript
/** Example 1: Example of void */
function logMessage(msg: string): void {
  console.log(msg);
}
type Logger = (msg: string) => void;

/** Example 2: Example of undefined */
function findItem(id: number): Item | undefined {
  return items.find(item => item.id === id);
}

/** Example 3: Runtime comparison */
console.log(logMessage("test"));
console.log(findItem(1));
```
