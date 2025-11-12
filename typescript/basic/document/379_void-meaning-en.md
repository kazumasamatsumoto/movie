# #379 "Meaning of void"

Shikoku Metan: "The void type signals that a function exists purely for side effects."
Zundamon: "updateUI is a perfect example because it only manipulates the DOM."
Shikoku Metan: "Exactly, no caller needs a return value there."
Zundamon: "Callbacks in forEach are void too since we ignore their return value?"
Shikoku Metan: "Right—callback: (item: T) => void authorizes side effects per item."
Zundamon: "Event handler types gain clarity when we include void."
Shikoku Metan: "Defining EventHandler = (event: Event) => void tells readers the result is ignored."
Zundamon: "I'll use void intentionally to communicate meaning!"

---

## 📺 Code for Display

```typescript
/** Example 1: Function for side effects */
function updateUI(data: Data): void {
  document.getElementById("app")!.innerHTML = data.html;
}

/** Example 2: Callback function */
function forEach<T>(
  array: T[],
  callback: (item: T) => void
): void {
  for (const item of array) {
    callback(item);
  }
}

/** Example 3: Handlers that ignore returns */
type EventHandler = (event: Event) => void;
element.addEventListener("click", (e): void => {
  console.log("Clicked", e);
});
```
