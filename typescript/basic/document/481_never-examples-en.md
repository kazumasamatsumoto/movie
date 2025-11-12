# #481 "Use Cases"

Shikoku Metan: "never shines in validation and error handlers."
Zundamon: "validatePositive threw whenever the input was invalid."
Shikoku Metan: "Assertions like assertDefined combine with never to narrow types."
Zundamon: "handleError even called process.exit(1)!"
Shikoku Metan: "Grouping non-returning logic keeps code reusable."
Zundamon: "I will model real-world never use cases."

---

## 📺 Code for Display

```typescript
/** Example 1: Validation */
function validatePositive(value: number): void {
  if (value <= 0) {
    throwError("Value must be positive");
  }
}

function throwError(message: string): never {
  throw new Error(message);
}

/** Example 2: Assertion */
function assertDefined<T>(value: T | undefined): asserts value is T {
  if (value === undefined) {
    throw new Error("Value is undefined");
  }
}

/** Example 3: Error handler */
function handleError(error: unknown): never {
  console.error("Fatal error:", error);
  process.exit(1);
}
```
