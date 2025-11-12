# #490 "Exception Summary"

Shikoku Metan: "Here's the wrap-up for never and exceptions."
Zundamon: "fail(message) is the staple throwing function."
Shikoku Metan: "Pair it with assertNever for exhaustiveness."
Zundamon: "We also saw custom errors handled via try-catch."
Shikoku Metan: "Review these patterns to master never-based errors."

---

## 📺 Code for Display

```typescript
/** Example 1: Throwing function */
function fail(message: string): never {
  throw new Error(message);
}

/** Example 2: Exhaustive check */
function assertNever(value: never): never {
  throw new Error(`Unhandled: ${value}`);
}

/** Example 3: Custom error try-catch */
class AppError extends Error {}
try {
  throw new AppError("Error");
} catch (error) {
  if (error instanceof AppError) {
    console.error(error.message);
  }
}
```
