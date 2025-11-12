# #479 "Custom Errors"

Shikoku Metan: "Custom errors clarify what a never function signals."
Zundamon: "We threw ValidationError and NotFoundError."
Shikoku Metan: "Attach field names or IDs for debugging."
Zundamon: "Perfect for validation helpers returning never!"
Shikoku Metan: "Treat error design as part of the type system."

---

## 📺 Code for Display

```typescript
/** Example 1: Define custom error */
class ValidationError extends Error {
  constructor(public field: string, message: string) {
    super(message);
    this.name = "ValidationError";
  }
}

/** Example 2: Throw custom error */
function validateAge(age: number): never {
  throw new ValidationError("age", "Age must be positive");
}

/** Example 3: Multiple error types */
class NotFoundError extends Error {
  constructor(public id: string) {
    super(`Resource ${id} not found`);
    this.name = "NotFoundError";
  }
}
function findUser(id: string): never {
  throw new NotFoundError(id);
}
```
