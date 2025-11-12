# #393 "Event Handlers"

Shikoku Metan: "Event handlers are classic void functions."
Zundamon: "The button?.addEventListener example just logs the click position."
Shikoku Metan: "Right, it prints coordinates and returns nothing."
Zundamon: "Can we define EventHandler = (event: Event) => void as a reusable type?"
Shikoku Metan: "Absolutely; it's handy when calling preventDefault."
Zundamon: "React's handleClick should also declare (e: React.MouseEvent): void."
Shikoku Metan: "Yes, then JSX onClick can consume it directly."
Zundamon: "I'll keep void handlers consistent across frameworks!"

---

## 📺 Code for Display

```typescript
/** Example 1: DOM event */
const button = document.getElementById("btn");
button?.addEventListener("click", (e: MouseEvent): void => {
  console.log("Clicked at:", e.clientX, e.clientY);
});

/** Example 2: Type definition */
type EventHandler = (event: Event) => void;
const handler: EventHandler = (e) => {
  e.preventDefault();
  console.log("Event handled");
};

/** Example 3: React event */
const handleClick = (e: React.MouseEvent): void => {
  console.log("Button clicked");
};
<button onClick={handleClick}>Click</button>
```
