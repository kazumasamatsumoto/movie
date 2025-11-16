# #483 "try-catch"

Shikoku Metan: "Handle never functions with try-catch when needed."
Zundamon: "riskyOperation() always threw."
Shikoku Metan: "Use instanceof for custom errors."
Zundamon: "We can check against Error as well?"
Shikoku Metan: "Yes, narrow the type inside catch."

---

## 📺 Code for Display

```typescript
/** Example 1: try-catch with never */
function riskyOperation(): never {
  throw new Error("Operation failed");
}
try {
  riskyOperation();
} catch (error) {
  console.error("Caught:", error);
}

/** Example 2: Custom error catch */
class ValidationError extends Error {}
function validate(data: unknown): never {
  throw new ValidationError("Invalid");
}
try {
  validate(data);
} catch (error) {
  if (error instanceof ValidationError) {
    console.error("Validation failed");
  }
}

/** Example 3: Error type check */
try {
  throwError("Error");
} catch (error) {
  if (error instanceof Error) {
    console.error(error.message);
  }
}
```
