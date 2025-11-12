# #463 "Exception Throwing Functions"

Shikoku Metan: "Functions that throw should return never."
Zundamon: "Like throwError(message)."
Shikoku Metan: "assert-style helpers also become never on failure."
Zundamon: "divide() called throwError when dividing by zero."
Shikoku Metan: "Declaring never makes callers aware that execution stops."

---

## 📺 Code for Display

```typescript
/** Example 1: Throwing function */
function throwError(message: string): never {
  throw new Error(message);
}

/** Example 2: Assertion function */
function assert(condition: boolean, message: string): asserts condition {
  if (!condition) {
    throw new Error(message);
  }
}

/** Example 3: Usage example */
function divide(a: number, b: number): number {
  if (b === 0) {
    throwError("Division by zero");
  }
  return a / b;
}
```
