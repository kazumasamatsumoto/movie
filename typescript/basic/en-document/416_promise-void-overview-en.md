# #416 "What Is Promise<void>"

Shikoku Metan: "Void also appears in async code via Promise<void>."
Zundamon: "saveData returned Promise<void> in the example."
Shikoku Metan: "Yes, it simply signals completion."
Zundamon: "Does async function initialize() infer Promise<void> automatically?"
Shikoku Metan: "As long as it returns nothing, yes."
Zundamon: "main also returned Promise<void> and just logged completion!"
Shikoku Metan: "Promise<void> is perfect for side-effect-heavy async flows."
Zundamon: "I'll apply the void mindset even in async code!"

---

## 📺 Code for Display

```typescript
/** Example 1: Basic Promise<void> */
async function saveData(data: Data): Promise<void> {
  await database.save(data);
  console.log("Saved");
}

/** Example 2: Type inference */
async function initialize() {
  await loadConfig();
  await connectDB();
}

/** Example 3: Usage */
async function main(): Promise<void> {
  await saveData({ id: 1, name: "Alice" });
  console.log("Complete");
}
```
