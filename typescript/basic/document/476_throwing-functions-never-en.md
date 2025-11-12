# #476 "Functions with throw"

Shikoku Metan: "Functions that throw should return never."
Zundamon: "fail(message) demonstrates that pattern."
Shikoku Metan: "assert(condition) also narrows types because failures are never."
Zundamon: "divide() called throwError when dividing by zero."
Shikoku Metan: "Express error behavior via types to help consumers."

---

## 📺 Code for Display

```typescript
/** Example 1: throwError */
function throwError(message: string): never {
  throw new Error(message);
}

/** Example 2: Assertion */
function assert(condition: boolean, message: string): asserts condition {
  if (!condition) {
    throw new Error(message);
  }
}

/** Example 3: Usage */
function divide(a: number, b: number): number {
  if (b === 0) {
    throwError("Division by zero");
  }
  return a / b;
}
```
