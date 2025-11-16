# #421 "await"

Shikoku Metan: "Use await to wait for Promise<void> completion."
Zundamon: "process awaited saveData and logActivity in order."
Shikoku Metan: "Right, each step finishes before the next begins."
Zundamon: "The await expression itself has type void, so we don't use the value?"
Shikoku Metan: "Exactly—assign it to const result: void if you need to show intent."
Zundamon: "It's perfect for sequential flows like step1 → step2 → step3."
Shikoku Metan: "await keeps the code readable while staying asynchronous."
Zundamon: "I'll rely on await to express intuitive async logic!"

---

## 📺 Code for Display

```typescript
/** Example 1: Waiting with await */
async function process(): Promise<void> {
  await saveData(data);
  await logActivity("Saved");
  console.log("All done");
}

/** Example 2: await result is void */
async function example(): Promise<void> {
  const result: void = await initialize();
}

/** Example 3: Sequential execution */
async function sequence(): Promise<void> {
  await step1();
  await step2();
  await step3();
}
```
