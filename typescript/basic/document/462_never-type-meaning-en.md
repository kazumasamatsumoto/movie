# #462 "Meaning of never"

Shikoku Metan: "never explicitly states that execution never continues."
Zundamon: "The fail function threw an error to stop everything."
Shikoku Metan: "Server main loops that run forever are never too."
Zundamon: "Can we use it to ensure switch statements are exhaustive?"
Shikoku Metan: "Yes, calling fail("Unreachable") signals that the rest is impossible."
Zundamon: "So never helps both type checking and runtime flow."

---

## 📺 Code for Display

```typescript
/** Example 1: Stop via exception */
function fail(message: string): never {
  throw new Error(message);
}

/** Example 2: Endless serve loop */
function serve(): never {
  while (true) {
    handleRequest();
  }
}

/** Example 3: Mark unreachable */
function process(value: string | number): string {
  if (typeof value === "string") {
    return value.toUpperCase();
  } else if (typeof value === "number") {
    return value.toString();
  }
  return fail("Unreachable");
}
```
