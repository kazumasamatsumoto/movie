# #474 "Use Cases"

Shikoku Metan: "never shines in exhaustive checks and error flows."
Zundamon: "exhaustiveCheck(value: never) is super handy!"
Shikoku Metan: "Switch statements error out when a case is missing."
Zundamon: "assertNonNull throws so unhandled branches are never."
Shikoku Metan: "This guards runtime and compile-time behavior."
Zundamon: "I will memorize these practical patterns!"

---

## 📺 Code for Display

```typescript
/** Example 1: Exhaustive switch */
function exhaustiveCheck(value: never): never {
  throw new Error(`Unhandled case: ${value}`);
}
type Status = "pending" | "success" | "error";
function handleStatus(status: Status): void {
  switch (status) {
    case "pending": return;
    case "success": return;
    case "error": return;
    default: exhaustiveCheck(status);
  }
}

/** Example 2: Error handling */
function assertNonNull<T>(value: T | null): asserts value is T {
  if (value === null) {
    throw new Error("Value is null");
  }
}

/** Example 3: Unreachable detection */
function unreachable(value: never): never {
  throw new Error(`Unexpected: ${value}`);
}
```
