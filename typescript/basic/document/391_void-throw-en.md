# #391 "Throw Statements"

Shikoku Metan: "Void functions can still throw exceptions."
Zundamon: "So assert throws new Error when the condition fails."
Shikoku Metan: "Exactly; even side-effect functions should signal errors via throws."
Zundamon: "validateAge shows multiple if checks to keep the logic readable!"
Shikoku Metan: "Whenever a value crosses the boundary we throw immediately."
Zundamon: "throwError returns never, so a void function can call it safely?"
Shikoku Metan: "Right—never is assignable to void, so process can delegate to it."
Zundamon: "I'll understand throw semantics to keep void functions safe!"

---

## 📺 Code for Display

```typescript
/** Example 1: Throw inside a void function */
function assert(condition: boolean, message: string): void {
  if (!condition) {
    throw new Error(message);
  }
}

/** Example 2: Validation function */
function validateAge(age: number): void {
  if (age < 0) throw new Error("Age cannot be negative");
  if (age > 150) throw new Error("Age is too large");
  console.log("Age is valid");
}

/** Example 3: Relation to never */
function throwError(message: string): never {
  throw new Error(message);
}
function process(): void {
  throwError("Error");
}
```
