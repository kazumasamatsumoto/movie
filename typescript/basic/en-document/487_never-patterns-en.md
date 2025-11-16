# #487 "Patterns"

Shikoku Metan: "Memorize common never patterns."
Zundamon: "Exhaustive checks, assertions, and notImplemented were the big three."
Shikoku Metan: "Each ends execution without returning."
Zundamon: "Templates make reuse easy."
Shikoku Metan: "Customize them to your project."

---

## 📺 Code for Display

```typescript
/** Example 1: Exhaustive check */
function assertNever(value: never): never {
  throw new Error(`Unhandled case: ${value}`);
}

/** Example 2: Assertion */
function assert(condition: boolean, message: string): asserts condition {
  if (!condition) throw new Error(message);
}

/** Example 3: notImplemented helper */
function notImplemented(feature: string): never {
  throw new Error(`${feature} is not implemented`);
}
```
