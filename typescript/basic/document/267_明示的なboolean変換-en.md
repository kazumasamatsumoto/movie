# #267 "Explicit Boolean Conversion"

Shikoku Metan: "Let's learn about explicit boolean conversion!"
Zundamon: "Using the Boolean() function, we can clearly convert values to true or false!"
Shikoku Metan: "That's right. As another method, the !! operator (double negation) is also commonly used."
Zundamon: "The !! operator uses ! twice, so it flips false to true, true to false, and then flips again?"
Shikoku Metan: "Exactly. As a result, we get the boolean representation of the original value."
Zundamon: "When creating type-safe functions, using Boolean() is more readable!"
Shikoku Metan: "It's especially useful when validating user input in conditional expressions."
Zundamon: "Explicit conversion makes the code's intent clearer than implicit conversion!"

---

## 📺 Code for Display

```typescript
/** Example 1: Boolean() function */
const value1 = Boolean('hello'); // true
const value2 = Boolean(0);       // false

/** Example 2: !! operator (double negation) */
const value3 = !!'hello';  // true
const value4 = !!0;        // false

/** Example 3: Type-safe conversion function */
function toBoolean(value: unknown): boolean {
  return Boolean(value);
}
```
