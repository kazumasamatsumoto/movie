# #424 "Error Handling"

Shikoku Metan: "Error handling matters even for Promise<void>."
Zundamon: "We wrapped saveData and notify in try-catch."
Shikoku Metan: "Yes, you can also use the catch() method."
Zundamon: "The finally example ensured cleanup always runs!"
Shikoku Metan: "withCleanup performs cleanup after processData no matter what."
Zundamon: "Designing for both success and failure is critical."
Shikoku Metan: "Async side effects need careful error handling."
Zundamon: "I'll never skip error planning even with void promises!"

---

## 📺 Code for Display

```typescript
/** Example 1: try-catch */
async function process(): Promise<void> {
  try {
    await saveData(data);
    await notify("Success");
  } catch (error) {
    console.error("Failed:", error);
  }
}

/** Example 2: catch() method */
saveData(data)
  .then(() => notify("Success"))
  .catch((error) => {
    console.error("Failed:", error);
  });

/** Example 3: finally block */
async function withCleanup(): Promise<void> {
  try {
    await processData();
  } catch (error) {
    console.error(error);
  } finally {
    await cleanup();
  }
}
```
