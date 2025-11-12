# #402 "void Means 'Don't Care About Values'"

Shikoku Metan: "void declares that we don't care about the return value."
Zundamon: "updateUI, which just calls render, is a good example."
Shikoku Metan: "Right—it makes it explicit that nothing is consumed."
Zundamon: "Using the result anyway triggers an error?"
Shikoku Metan: "Yes, assigning process() to a string fails."
Zundamon: "Callback = (data: string) => void also captures that behavior."
Shikoku Metan: "It signals a pure side-effect callback."
Zundamon: "I'll describe value-agnostic functions with void!"

---

## 📺 Code for Display

```typescript
/** Example 1: void: ignore values */
function updateUI(): void {
  render();
}

/** Example 2: Using the result is an error */
function process(): void {
  console.log("Processing");
}
const result: string = process();

/** Example 3: Callback */
type Callback = (data: string) => void;
const handler: Callback = (data) => {
  console.log(data);
};
```
