# #429 "Best Practices"

Shikoku Metan: "Let's recap best practices for Promise<void>."
Zundamon: "First, declare the return type explicitly."
Shikoku Metan: "Exactly—saveData(data): Promise<void>."
Zundamon: "Error handling is another pillar."
Shikoku Metan: "process wrapped its logic with try-catch-finally."
Zundamon: "And leverage Promise.all for parallel work."
Shikoku Metan: "processAll maps items and awaits Promise.all for efficiency."
Zundamon: "I'll follow these guidelines for robust Promise<void> code!"

---

## 📺 Code for Display

```typescript
/** Example 1: Explicit return */
async function saveData(data: Data): Promise<void> {
  await database.save(data);
}

/** Example 2: Error handling */
async function process(): Promise<void> {
  try {
    await processData();
  } catch (error) {
    console.error("Failed:", error);
    throw error;
  } finally {
    await cleanup();
  }
}

/** Example 3: Parallel execution */
async function processAll(items: Item[]): Promise<void> {
  await Promise.all(items.map(item => saveItem(item)));
}
```
