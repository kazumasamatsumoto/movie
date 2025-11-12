# #486 "Designing Error Functions"

Shikoku Metan: "Name and structure error functions carefully."
Zundamon: "throwValidationError(field, reason) was very clear!"
Shikoku Metan: "assertPositive forwarded context to the caller."
Zundamon: "createError(type, message) boosted reusability."
Shikoku Metan: "Well-designed never functions improve maintainability."

---

## 📺 Code for Display

```typescript
/** Example 1: Clear naming */
function throwValidationError(field: string, reason: string): never {
  throw new Error(`Validation failed for ${field}: ${reason}`);
}

/** Example 2: Include context */
function assertPositive(value: number, name: string): void {
  if (value <= 0) {
    throwError(`${name} must be positive, got ${value}`);
  }
}
function throwError(message: string): never {
  throw new Error(message);
}

/** Example 3: Reusable helper */
function createError(type: string, message: string): never {
  throw new Error(`[${type}] ${message}`);
}
function validateUser(user: unknown): void {
  if (!user) {
    createError("VALIDATION", "User is required");
  }
}
```
