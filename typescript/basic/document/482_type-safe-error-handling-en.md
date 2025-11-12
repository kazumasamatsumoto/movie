# #482 "Type-Safe Error Handling"

Shikoku Metan: "never delivers type-safe error flows."
Zundamon: "processData threw when data was null."
Shikoku Metan: "Combine it with custom errors for more detail."
Zundamon: "ensure() removed null safely."
Shikoku Metan: "Handle failures and narrow types at the same time."
Zundamon: "I will practice type-safe error design with never!"

---

## 📺 Code for Display

```typescript
/** Example 1: Handling errors safely */
function processData(data: string | null): string {
  if (data === null) {
    throwError("Data is null");
  }
  return data.toUpperCase();
}
function throwError(message: string): never {
  throw new Error(message);
}

/** Example 2: Custom error */
class InvalidDataError extends Error {
  constructor(public data: unknown) {
    super("Invalid data");
  }
}
function validateData(data: unknown): never {
  throw new InvalidDataError(data);
}

/** Example 3: Narrowing helper */
function ensure<T>(value: T | null, message: string): T {
  if (value === null) {
    throwError(message);
  }
  return value;
}
```
