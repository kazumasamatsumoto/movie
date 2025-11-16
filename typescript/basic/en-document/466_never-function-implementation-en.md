# #466 "Implementing never Functions"

Shikoku Metan: "never functions must never return control."
Zundamon: "fail threw, loop ran forever."
Shikoku Metan: "If you log and return, the compiler downgrades it to void."
Zundamon: "invalid() showed that mistake."
Shikoku Metan: "Types flag violations immediately."
Zundamon: "So never functions should only throw or loop!"

---

## 📺 Code for Display

```typescript
/** Example 1: Throw implementation */
function fail(message: string): never {
  throw new Error(message);
}

/** Example 2: Infinite loop */
function loop(): never {
  while (true) {
    doWork();
  }
}

/** Example 3: Invalid example */
function invalid(): never {
  console.log("Error");
  // return;
}
```
