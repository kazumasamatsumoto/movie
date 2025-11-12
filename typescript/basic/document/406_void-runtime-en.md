# #406 "Actual Return Values"

Shikoku Metan: "Even void functions return undefined at runtime."
Zundamon: "Printing log('Hello') showed undefined!"
Shikoku Metan: "Right, but the type system still treats it as void."
Zundamon: "So const value: void = log('Test') works?"
Shikoku Metan: "Yes, but assigning it to string does not."
Zundamon: "In JavaScript the transpiled function f1(): void also returns undefined."
Shikoku Metan: "Exactly—function f1() {} behaves the same."
Zundamon: "I'll separate runtime behavior from type-level intent!"

---

## 📺 Code for Display

```typescript
/** Example 1: void type, undefined runtime */
function log(msg: string): void {
  console.log(msg);
}
const result = log("Hello");
console.log(result);
console.log(typeof result);

/** Example 2: Type-level handling */
const value: void = log("Test");
// const str: string = log("Test");

/** Example 3: JavaScript output */
function f1(): void {}
// JavaScript output
function f1() {}
```
