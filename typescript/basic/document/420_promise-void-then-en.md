# #420 "then() without Arguments"

Shikoku Metan: "Promise<void> lets us attach completion handlers via then()."
Zundamon: "We saw saveData(data).then(() => ...)."
Shikoku Metan: "Yes, the callback takes no arguments and just signals success."
Zundamon: "We can chain initialize().then(...).catch(...) too?"
Shikoku Metan: "Absolutely."
Zundamon: "Yet async/await is often cleaner."
Shikoku Metan: "Using await inside main keeps the flow readable."
Zundamon: "I'll switch between then and await as needed!"

---

## 📺 Code for Display

```typescript
/** Example 1: Waiting with then() */
saveData(data).then(() => {
  console.log("Save complete");
});

/** Example 2: Chaining with catch */
initialize().then(() => {
  console.log("Initialized");
}).catch((error) => {
  console.error("Failed:", error);
});

/** Example 3: async/await */
async function main() {
  await saveData(data);
  console.log("Save complete");
}
```
