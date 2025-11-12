# #518 "Best Practices"

Shikoku Metan: "Let's list exhaustiveness best practices."
Zundamon: "Start by centralizing assertNever() and exhaustiveCheck()."
Shikoku Metan: "unwrap() on Result returned value for success and threw on failures."
Zundamon: "Calling exhaustiveCheck(result) covers any new variant."
Shikoku Metan: "execute() dispatched save/load/delete via switch."
Zundamon: "The default branch returning exhaustiveCheck(action) keeps style consistent."
Shikoku Metan: "Shared helpers let every union follow the same structure."
Zundamon: "Spread those habits across the team."

---

## 📺 Code for Display

```typescript
/** Example 1: Helper functions */
function assertNever(value: never, message?: string): never {
  throw new Error(message ?? `Unexpected value: ${value}`);
}

function exhaustiveCheck(value: never): never {
  return assertNever(value, "Unhandled case");
}

/** Example 2: Result helper */
type Result<T, E> =
  | { success: true; value: T }
  | { success: false; error: E };

function unwrap<T, E>(result: Result<T, E>): T {
  if (result.success) return result.value;
  if (!result.success) throw result.error;
  return exhaustiveCheck(result);
}

/** Example 3: switch pattern */
type Action = "save" | "load" | "delete";

function execute(action: Action): void {
  switch (action) {
    case "save":
      return save();
    case "load":
      return load();
    case "delete":
      return remove();
    default:
      return exhaustiveCheck(action);
  }
}
```
