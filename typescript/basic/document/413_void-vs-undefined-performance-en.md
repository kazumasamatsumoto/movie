# #413 "Performance"

Shikoku Metan: "There is no performance difference between void and undefined."
Zundamon: "We saw both voidFunc and undefFunc in TypeScript."
Shikoku Metan: "Right, the emitted JavaScript looks nearly identical."
Zundamon: "console.log(voidFunc()) and console.log(undefFunc()) both printed undefined!"
Shikoku Metan: "Exactly—the types disappear at compile time."
Zundamon: "So I only need to consider semantics, not speed."
Shikoku Metan: "Correct; choose types for meaning, not performance."
Zundamon: "I'll pick void or undefined based on intent!"

---

## 📺 Code for Display

```typescript
/** Example 1: TypeScript code */
function voidFunc(): void {
  console.log("void");
}
function undefFunc(): undefined {
  return undefined;
}

/** Example 2: JavaScript output */
function voidFunc() {
  console.log("void");
}
function undefFunc() {
  return undefined;
}

/** Example 3: Runtime behavior */
console.log(voidFunc());
console.log(undefFunc());
```
