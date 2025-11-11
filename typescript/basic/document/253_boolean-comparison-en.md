# #253 "Boolean Comparison"

Shikoku Metan: "Let's learn about boolean comparison!"
Zundamon: "We compare true with true, and false with false, right!"
Shikoku Metan: "Yes. Using the strict equality operator === is the basic approach."
Zundamon: "true === true is true, and true === false is false!"
Shikoku Metan: "Exactly. The results can differ between == and ===."
Zundamon: "Does true == 1 return true?"
Shikoku Metan: "Yes. == performs type coercion, but === compares types strictly."
Zundamon: "Creating type-safe comparison functions and handling them explicitly is important!"

---

## 📺 Code for Display

```typescript
/** Example 1: Strict comparison */
console.log(true === true);   // true
console.log(false === false); // true
console.log(true === false);  // false

/** Example 2: Type differences */
console.log(true === 1);  // false
console.log(true == 1);   // true

/** Example 3: Type-safe comparison function */
function isSameBoolean(a: boolean, b: boolean): boolean {
  return a === b;
}
```
