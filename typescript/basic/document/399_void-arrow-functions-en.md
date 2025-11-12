# #399 "Arrow Functions"

Shikoku Metan: "Arrow functions can also be annotated with void."
Zundamon: "const log = (msg: string): void => {...} is the simplest example."
Shikoku Metan: "Right, it clarifies that no result is used."
Zundamon: "Can we assign them to a VoidFunction = (x: number) => void alias?"
Shikoku Metan: "Yes, the double function demonstrates that."
Zundamon: "You can even add : void on anonymous forEach arrows."
Shikoku Metan: "It improves readability for side-effect-only callbacks."
Zundamon: "I won't forget void on arrow functions!"

---

## 📺 Code for Display

```typescript
/** Example 1: Void arrow function */
const log = (msg: string): void => {
  console.log(msg);
};

/** Example 2: Using a type alias */
type VoidFunction = (x: number) => void;
const double: VoidFunction = (x) => {
  console.log(x * 2);
};

/** Example 3: Array method */
const items = [1, 2, 3];
items.forEach((item): void => {
  console.log(item);
});
```
