# #485 "Debugging"

Shikoku Metan: "Instrument never functions for debugging."
Zundamon: "fail logged context and console.trace."
Shikoku Metan: "assertNever printed extra info when DEBUG was true."
Zundamon: "We even paused with debugger before throwing."
Shikoku Metan: "Leave clues because execution stops there."

---

## 📺 Code for Display

```typescript
/** Example 1: Debug logging */
function fail(message: string, context?: unknown): never {
  console.error("Error context:", context);
  console.trace();
  throw new Error(message);
}

/** Example 2: Conditional debug */
const DEBUG = true;
function assertNever(value: never): never {
  if (DEBUG) {
    console.error("Unexpected value:", value);
  }
  throw new Error(`Unhandled case: ${value}`);
}

/** Example 3: Debugger break */
function throwError(message: string): never {
  debugger;
  throw new Error(message);
}
```
