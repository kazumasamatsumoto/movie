# #423 "Promise<void> Chaining"

Shikoku Metan: "You can chain Promise<void> with then()."
Zundamon: "saveData().then(...).then(...) demonstrated that."
Shikoku Metan: "Yes, catch consolidates error handling."
Zundamon: "Is it clearer when rewritten with async/await?"
Shikoku Metan: "Exactly—process shows the sequential await style."
Zundamon: "Even initialize().then(...).then(...) still has type Promise<void>."
Shikoku Metan: "The entire chain evaluates to Promise<void>."
Zundamon: "I'll choose between chaining and await based on readability!"

---

## 📺 Code for Display

```typescript
/** Example 1: Chaining */
saveData(data)
  .then(() => logActivity("Saved"))
  .then(() => notify("Complete"))
  .catch((error) => console.error(error));

/** Example 2: async/await alternative */
async function process(): Promise<void> {
  await saveData(data);
  await logActivity("Saved");
  await notify("Complete");
}

/** Example 3: Type of chain */
const promise: Promise<void> = initialize()
  .then(() => loadData())
  .then(() => render());
```
