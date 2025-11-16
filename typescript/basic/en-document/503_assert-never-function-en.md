# #503 "Exhaustive Helper Functions"

Shikoku Metan: "Let's craft a dedicated exhaustive helper."
Zundamon: "assertNever(value: never) threw an 'Unexpected value' error."
Shikoku Metan: "In getArea() we simply return assertNever(shape) in default."
Zundamon: "Adding circles or squares later highlights the missing logic."
Shikoku Metan: "exhaustiveCheck() lets us swap in custom messages."
Zundamon: "JSON.stringify(value) boosts the debugging detail."
Shikoku Metan: "Once it's a utility, every union reads the same."
Zundamon: "Build the foundation early to ease future refactors."

---

## 📺 Code for Display

```typescript
/** Example 1: Defining assertNever */
function assertNever(value: never): never {
  throw new Error(`Unexpected value: ${value}`);
}

/** Example 2: Shape area calculation */
type Shape = "circle" | "square" | "triangle";

function getArea(shape: Shape): number {
  switch (shape) {
    case "circle":
      return Math.PI;
    case "square":
      return 1;
    case "triangle":
      return 0.5;
    default:
      return assertNever(shape);
  }
}

/** Example 3: Custom error messages */
function exhaustiveCheck(value: never, message?: string): never {
  throw new Error(message || `Unhandled discriminated union member: ${JSON.stringify(value)}`);
}
```
