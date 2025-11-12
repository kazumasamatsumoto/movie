# #430 "Async void Summary"

Shikoku Metan: "Let's wrap up the Promise<void> chapter."
Zundamon: "Functions like saveData perform side effects and signal completion."
Shikoku Metan: "Yes, await lets us express sequential flows."
Zundamon: "processAll used Promise.all for parallel execution!"
Shikoku Metan: "It's great for waiting on multiple tasks."
Zundamon: "I feel confident designing async void functions now."
Shikoku Metan: "Remember side effects, await, and concurrency as the core pillars."
Zundamon: "I'll master Promise<void> with this summary!"

---

## 📺 Code for Display

```typescript
/** Example 1: Promise<void> basics */
async function saveData(data: Data): Promise<void> {
  await database.save(data);
  console.log("Saved");
}

/** Example 2: Await completion */
async function process(): Promise<void> {
  await saveData(data);
  await logActivity("Complete");
}

/** Example 3: Parallel execution */
async function processAll(): Promise<void> {
  await Promise.all([task1(), task2(), task3()]);
  console.log("All complete");
}
```
