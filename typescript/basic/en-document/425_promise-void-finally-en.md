# #425 "finally()"

Shikoku Metan: "finally runs regardless of success or failure."
Zundamon: "We wrote saveData().finally(() => Cleanup)."
Shikoku Metan: "Yes, try-catch-finally achieves the same with async/await."
Zundamon: "The loading indicator example was nice too!"
Shikoku Metan: "loadData shows loading, fetches, then hides loading in finally."
Zundamon: "So finally guarantees cleanup for Promise<void>."
Shikoku Metan: "It's a key safeguard for async side effects."
Zundamon: "I'll place must-run logic inside finally!"

---

## 📺 Code for Display

```typescript
/** Example 1: finally() method */
saveData(data)
  .then(() => console.log("Success"))
  .catch((error) => console.error(error))
  .finally(() => {
    console.log("Cleanup");
  });

/** Example 2: async/await finally */
async function process(): Promise<void> {
  try {
    await saveData(data);
  } catch (error) {
    console.error(error);
  } finally {
    await cleanup();
  }
}

/** Example 3: Loading indicator */
async function loadData(): Promise<void> {
  showLoading();
  try {
    await fetchData();
  } finally {
    hideLoading();
  }
}
```
