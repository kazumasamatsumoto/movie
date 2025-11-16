# #266 "Truthy Values"

Shikoku Metan: "Let's learn about truthy values!"
Zundamon: "So in JavaScript, there are values that are treated as true even though they're not actually true!"
Shikoku Metan: "That's right. Numbers like 1, non-empty strings, arrays, and objects are truthy."
Zundamon: "0 and empty strings are false, but the string '0' becomes true?"
Shikoku Metan: "Exactly. If it contains a string, it's judged as truthy."
Zundamon: "It's surprising that empty arrays [] and empty objects {} are also truthy!"
Shikoku Metan: "It's commonly used when checking the existence of values in conditional branches, so let's remember it."
Zundamon: "Using the Boolean() function, we can convert any value to true or false!"

---

## 📺 Code for Display

```typescript
/** Example 1: Basic truthy values */
console.log(Boolean(1));         // true
console.log(Boolean('hello'));   // true
console.log(Boolean('0'));       // true (string '0')

/** Example 2: Objects and arrays */
console.log(Boolean([]));        // true (empty array)
console.log(Boolean({}));        // true (empty object)

/** Example 3: Functions and Date */
console.log(Boolean(function(){})); // true
console.log(Boolean(new Date())); // true
```
