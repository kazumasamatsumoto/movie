# #371 "What Is the void Type"

Shikoku Metan: "Use the void type when a function's return value does not matter."
Zundamon: "Declaring function logMessage(msg: string): void signals it's just logging!"
Shikoku Metan: "Right, you can omit return entirely and focus on side effects."
Zundamon: "How is that different from a function returning undefined?"
Shikoku Metan: "void means 'nothing is returned', while undefined means 'the undefined value is returned.'"
Zundamon: "Should event listener callbacks also use void?"
Shikoku Metan: "Yes, () => void clearly states the callback only performs side effects."
Zundamon: "I'll rely on void whenever I want to highlight that no result is needed!"

---

## 📺 Code for Display

```typescript
/** Example 1: Void type basics */
function logMessage(msg: string): void {
  console.log(msg);
  // No return value or just return;
}

/** Example 2: Difference from undefined */
function returnsVoid(): void {
  console.log("Side effects only");
}
function returnsUndefined(): undefined {
  return undefined;  // Explicit undefined value
}

/** Example 3: Practical example */
function addEventListener(callback: () => void): void {
  // Register the event listener
}
```
