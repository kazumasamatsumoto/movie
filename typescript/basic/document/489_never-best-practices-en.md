# #489 "Best Practices"

Shikoku Metan: "Review never best practices."
Zundamon: "Provide explicit helpers like throwError or assertNever."
Shikoku Metan: "Custom errors convey context."
Zundamon: "Exhaustive checks round out the set."
Shikoku Metan: "Together they form a solid error strategy."

---

## 📺 Code for Display

```typescript
/** Example 1: Explicit helpers */
function throwError(message: string): never {
  throw new Error(message);
}
function assertNever(value: never): never {
  throw new Error(`Unexpected: ${value}`);
}

/** Example 2: Detailed error */
class ValidationError extends Error {
  constructor(public field: string, message: string) {
    super(`${field}: ${message}`);
  }
}
function validate(field: string, value: unknown): never {
  throw new ValidationError(field, "Invalid value");
}

/** Example 3: Exhaustive check */
type Status = "idle" | "loading" | "success" | "error";
function handleStatus(status: Status): void {
  switch (status) {
    case "idle":
    case "loading":
    case "success":
    case "error":
      return;
    default:
      assertNever(status);
  }
}
```
