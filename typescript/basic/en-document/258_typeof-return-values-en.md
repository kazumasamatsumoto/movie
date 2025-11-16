# #258 "Typeof Return Values"

Shikoku Metan: "Let's learn about typeof return values!"
Zundamon: "What strings does typeof return?"
Shikoku Metan: "It returns 'string', 'number', 'boolean', 'object', etc."
Zundamon: "Arrays also become object, right?"
Shikoku Metan: "Yes. And as a caveat, null also returns object."
Zundamon: "typeof null === 'object' is a famous bug, right!"
Shikoku Metan: "Exactly. Use === for null checks."
Zundamon: "Creating isNull with a type predicate function allows explicit checking!"

---

## 📺 Code for Display

```typescript
/** Example 1: typeof return values */
console.log(typeof 'hello');     // 'string'
console.log(typeof 42);          // 'number'
console.log(typeof true);        // 'boolean'
console.log(typeof {});          // 'object'
console.log(typeof []);          // 'object' (arrays too)
console.log(typeof null);        // 'object' (caution!)
console.log(typeof undefined);   // 'undefined'
console.log(typeof function(){}); // 'function'

/** Example 2: Correct null check */
function isNull(value: unknown): value is null {
  return value === null;
}
```
