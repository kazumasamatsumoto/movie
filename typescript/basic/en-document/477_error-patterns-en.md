# #477 "Type-Safe Error Patterns"

Shikoku Metan: "never helps keep error flows type-safe."
Zundamon: "exhaustiveCheck turned omissions into compile errors."
Shikoku Metan: "assertNever follows the same idea."
Zundamon: "I will systematize my error design with never!"

---

## 📺 Code for Display

```typescript
/** Example 1: Exhaustive helper */
function exhaustiveCheck(value: never): never {
  throw new Error(`Unhandled case: ${value}`);
}

/** Example 2: assertNever */
function assertNever(value: never): never {
  throw new Error(`Unexpected value: ${value}`);
}

/** Example 3: Usage example */
type Status = "pending" | "success";
function handleStatus(status: Status): void {
  switch (status) {
    case "pending": return;
    case "success": return;
    default: assertNever(status);
  }
}
```
