# #546 "Mistake (1) - Confusing void"

Shikoku Metan: "Mixing up void and never is dangerous."
Zundamon: "logMessage() returns normally and its result is void."
Shikoku Metan: "throwError() never returns, so its type must be never."
Zundamon: "Declaring process() as void but always throwing hides intent."
Shikoku Metan: "processCorrect() declares never so the compiler understands."
Zundamon: "void values are compatible with undefined; never isn't compatible with anything."
Shikoku Metan: "const d: never = undefined; rightfully fails."
Zundamon: "Use never for functions that never come back."

---

## 📺 Code for Display

```typescript
/** Example 1: void vs never */
function logMessage(msg: string): void {
  console.log(msg);
}

function throwError(msg: string): never {
  throw new Error(msg);
}
```

```typescript
/** Example 2: Wrong void usage */
function process(): void {
  throw new Error("Error");
}

function processCorrect(): never {
  throw new Error("Error");
}
```

```typescript
/** Example 3: Assignments */
const a: void = logMessage("Hello"); // OK
const b: never = throwError("Error"); // never returns

const c: void = undefined; // OK
const d: never = undefined; // Error
```
