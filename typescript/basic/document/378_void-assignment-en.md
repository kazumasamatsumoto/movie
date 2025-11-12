# #378 "Assigning to void"

Shikoku Metan: "Let's check which values assign to a void variable."
Zundamon: "Only undefined fits into value: void, right?"
Shikoku Metan: "That's right; null or numbers immediately cause type errors."
Zundamon: "The sample even commented the invalid assignments for clarity."
Shikoku Metan: "Be extra careful under strictNullChecks."
Zundamon: "If a function returns void, does assigning its result yield undefined?"
Shikoku Metan: "Yes, calling doSomething(): void and storing it in const result: void is consistent."
Zundamon: "Understanding these assignment rules prevents surprising errors!"

---

## 📺 Code for Display

```typescript
/** Example 1: Allowed value */
let value: void;
value = undefined;  // OK

/** Example 2: Invalid assignments */
let value: void;
// value = null;       // Error under strictNullChecks
// value = 0;          // Error
// value = "string";   // Error

/** Example 3: Return value from a void function */
function doSomething(): void {
  console.log("Done");
}
const result: void = doSomething();  // undefined
```
