# #384 "Promise<void>"

Shikoku Metan: "Void appears in async code as Promise<void>."
Zundamon: "async function saveData(...): Promise<void> is the perfect example."
Shikoku Metan: "Right, we only report completion."
Zundamon: "Even async function initialize() gets inferred to Promise<void> when nothing is returned."
Shikoku Metan: "Exactly—lack of return values means Promise<void>."
Zundamon: "processAll awaits Promise.all and logs completion!"
Shikoku Metan: "Whenever async work has no value to return, Promise<void> is ideal."
Zundamon: "I'll keep void in mind for asynchronous side effects too!"

---

## 📺 Code for Display

```typescript
/** Example 1: Basic Promise<void> */
async function saveData(data: Data): Promise<void> {
  await database.save(data);
  console.log("Saved");
}

/** Example 2: Promise<void> via inference */
async function initialize() {
  await loadConfig();
  await connectDB();
  // Inferred as Promise<void>
}

/** Example 3: Practical example */
async function processAll(items: Item[]): Promise<void> {
  await Promise.all(items.map(item => saveItem(item)));
  console.log("All items processed");
}
```
