# #392 "Callback Functions"

Shikoku Metan: "Void appears constantly in callbacks."
Zundamon: "Defining Callback = (data: string) => void keeps signatures tidy."
Shikoku Metan: "processAsync invokes callback('Done') when the work finishes."
Zundamon: "forEach callbacks don't return values either, right?"
Shikoku Metan: "Exactly; logging is a pure side effect."
Zundamon: "Event listeners usually look like (e: Event): void => { ... }?"
Shikoku Metan: "Yes, they're designed purely for side effects."
Zundamon: "I'll shape my callback types with void in mind!"

---

## 📺 Code for Display

```typescript
/** Example 1: Defining a callback type */
type Callback = (data: string) => void;
function processAsync(callback: Callback): void {
  setTimeout(() => callback("Done"), 1000);
}

/** Example 2: Array forEach */
const items = ["a", "b", "c"];
items.forEach((item: string): void => {
  console.log(item);
});

/** Example 3: Event listener */
button.addEventListener("click", (e: Event): void => {
  console.log("Clicked");
});
```
