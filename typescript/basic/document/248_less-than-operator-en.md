# #248 "Less Than Operator - <"

Shikoku Metan: "Let's learn about the less than operator!"
Zundamon: "So with <, we can check if the left side is less than the right side!"
Shikoku Metan: "Yes. It works opposite to the greater than operator."
Zundamon: "5 < 10 is true, but 10 < 5 becomes false, right?"
Shikoku Metan: "Exactly. It also returns false when values are equal."
Zundamon: "Can we create type-safe comparison functions?"
Shikoku Metan: "Of course. Functions like isLess improve code readability."
Zundamon: "It's commonly used for score range checks, so let's master it!"

---

## 📺 Code for Display

```typescript
/** Example 1: Basic usage */
console.log(5 < 10);   // true
console.log(10 < 5);   // false
console.log(5 < 5);    // false

/** Example 2: Type-safe comparison function */
function isLess(a: number, b: number): boolean {
  return a < b;
}

/** Example 3: Range check */
const score: number = 75;
if (score < 80) {
  console.log('Passing grade');
}
```
