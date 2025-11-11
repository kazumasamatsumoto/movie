# #249 "Greater Than or Equal Operator - >="

Shikoku Metan: "Let's learn about the greater than or equal operator!"
Zundamon: ">= is read as 'greater than or equal', right!"
Shikoku Metan: "Yes. It returns true when the left side is greater than or equal to the right side."
Zundamon: "Both 10 >= 5 and 10 >= 10 return true?"
Shikoku Metan: "Exactly. The key point is that it includes the equal case."
Zundamon: "It's commonly used for minimum value checks!"
Shikoku Metan: "It's useful for boundary conditions like age limits and eligibility requirements."
Zundamon: "Understanding the difference between > and >= is important!"

---

## 📺 Code for Display

```typescript
/** Example 1: Basic usage */
console.log(10 >= 5);   // true
console.log(10 >= 10);  // true
console.log(5 >= 10);   // false

/** Example 2: Type-safe comparison function */
function isGreaterOrEqual(a: number, b: number): boolean {
  return a >= b;
}

/** Example 3: Minimum value check */
const age: number = 18;
if (age >= 18) {
  console.log('Adult');
}
```
