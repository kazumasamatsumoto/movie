# #426 "Parallel Execution"

Shikoku Metan: "Use Promise.all() to run Promise<void> in parallel."
Zundamon: "processAll awaited three saveUser calls at once."
Shikoku Metan: "Yes, it waits for all of them."
Zundamon: "initialize ran loadConfig and connectDatabase in parallel too!"
Shikoku Metan: "It shortens heavy startup work."
Zundamon: "If a task fails inside Promise.all, do we catch it?"
Shikoku Metan: "Wrap the await in try-catch like processWithError."
Zundamon: "I'll execute side effects efficiently with parallelism!"

---

## 📺 Code for Display

```typescript
/** Example 1: Parallel with Promise.all */
async function processAll(): Promise<void> {
  await Promise.all([
    saveUser(user1),
    saveUser(user2),
    saveUser(user3)
  ]);
  console.log("All saved");
}

/** Example 2: Initialization */
async function initialize(): Promise<void> {
  await Promise.all([
    loadConfig(),
    connectDatabase(),
    startCache()
  ]);
}

/** Example 3: Error handling */
async function processWithError(): Promise<void> {
  try {
    await Promise.all([task1(), task2(), task3()]);
  } catch (error) {
    console.error("One of the tasks failed:", error);
  }
}
```
