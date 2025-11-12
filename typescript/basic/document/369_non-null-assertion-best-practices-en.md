# #369 "Best Practices"

Shikoku Metan: "If we ever use !, we should follow best practices."
Zundamon: "First rule is to prefer type guards, right?"
Shikoku Metan: "Correct—verify element !== null before touching the DOM."
Zundamon: "We should also lean on Optional Chaining?"
Shikoku Metan: "Yes, weave patterns like user?.name ?? 'Unknown' into the code."
Zundamon: "And when ! is unavoidable we annotate why?"
Shikoku Metan: "Exactly; explaining that the root element always exists reassures readers."
Zundamon: "I'll establish guidelines so ! stays minimal!"

---

## 📺 Code for Display

```typescript
/** Example 1: Prefer type guards */
const element = document.getElementById("app");
if (element !== null) {
  element.innerHTML = "Hello";
}

/** Example 2: Use Optional Chaining */
const name = user?.name ?? "Unknown";
const result = data?.process()?.value;

/** Example 3: Document unavoidable uses */
// Guaranteed to exist when the app boots
const rootElement = document.getElementById("root")!;
ReactDOM.render(<App />, rootElement);
```
