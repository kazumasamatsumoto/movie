# #461 "What Is the never Type"

Shikoku Metan: "The never type marks code paths that never return."
Zundamon: "Functions that throw errors are the classic example."
Shikoku Metan: "Infinite loops also evaluate to never."
Zundamon: "So the difference from void is whether control continues?"
Shikoku Metan: "Exactly—void execution resumes, never does not."
Zundamon: "Nice to signal hazardous code via types."
Shikoku Metan: "Use never to state that a path is unreachable."

---

## 📺 Code for Display

```typescript
/** Example 1: Throwing an error */
function throwError(message: string): never {
  throw new Error(message);
}

/** Example 2: Infinite loop */
function infiniteLoop(): never {
  while (true) {
    console.log("Running...");
  }
}

/** Example 3: Difference from void */
function voidFunc(): void {
  console.log("Done");
}
function neverFunc(): never {
  throw new Error("Never returns");
}
```
