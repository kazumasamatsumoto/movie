# #470 "Difference from void"

Shikoku Metan: "Let's wrap up by contrasting void and never."
Zundamon: "voidFunc() runs and then continues."
Shikoku Metan: "neverFunc() throws, so nothing afterward executes."
Zundamon: "process() calling void still hits console.log."
Shikoku Metan: "Calling never leaves the rest unreachable."
Zundamon: "Choose the type based on whether control returns!"

---

## 📺 Code for Display

```typescript
/** Example 1: void returns */
function voidFunc(): void {
  console.log("Done");
}

/** Example 2: never does not return */
function neverFunc(): never {
  throw new Error("Never returns");
}

/** Example 3: Usage difference */
function process(): void {
  voidFunc();
  console.log("After void");
}
function fail(): void {
  neverFunc();
  console.log("Never reached");
}
```
