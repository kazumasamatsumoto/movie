# #372 "Where to Use void"

Shikoku Metan: "void shines whenever a function's goal is side effects."
Zundamon: "log(message: string): void is the classic logging helper!"
Shikoku Metan: "Exactly; it finishes work without producing a value."
Zundamon: "Do arrow-based event handlers also use void?"
Shikoku Metan: "Yes, writing () => void for button.addEventListener keeps intent clear."
Zundamon: "Async functions that resolve to Promise<void> exist too, right?"
Shikoku Metan: "They do—saveData just persists data and resolves with nothing."
Zundamon: "I'll pick void whenever side effects are the final goal!"

---

## 📺 Code for Display

```typescript
/** Example 1: Logging */
function log(message: string): void {
  console.log(`[LOG] ${message}`);
}

/** Example 2: Event handler */
button.addEventListener("click", (): void => {
  console.log("Clicked");
});

/** Example 3: Async usage */
async function saveData(data: Data): Promise<void> {
  await database.save(data);
  console.log("Saved");
}
```
