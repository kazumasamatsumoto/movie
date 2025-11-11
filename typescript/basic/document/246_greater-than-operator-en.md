# #246 "Greater Than Operator - >"

Shikoku Metan: "Let's learn about the greater than operator!"
Zundamon: "So with >, we can check if the left side is greater than the right side!"
Shikoku Metan: "That's right. While numeric comparison is the basic use, it also works with strings and Date objects."
Zundamon: "10 > 5 is true, but 5 > 5 becomes false, right?"
Shikoku Metan: "Exactly. For equal cases, use the greater than or equal operator >=."
Zundamon: "Creating type-safe comparison functions makes code more readable too!"
Shikoku Metan: "It's commonly used in conditional branches like age checks, so let's master it thoroughly."
Zundamon: "It's convenient that strings can also be compared in dictionary order, not just numbers!"

---

## 📺 Code for Display

```typescript
/** Example 1: Basic usage */
console.log(10 > 5);   // true
console.log(5 > 10);   // false
console.log(5 > 5);    // false

/** Example 2: Type-safe comparison function */
function isGreater(a: number, b: number): boolean {
  return a > b;
}

/** Example 3: Usage in conditional branches */
const age: number = 20;
if (age > 18) {
  console.log('Adult');
}
```
