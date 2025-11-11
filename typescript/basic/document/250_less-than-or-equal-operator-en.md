# #250 "Less Than or Equal Operator - <="

Shikoku Metan: "Let's learn about the less than or equal operator!"
Zundamon: "<= is read as 'less than or equal', right!"
Shikoku Metan: "Yes. It returns true when the left side is less than or equal to the right side."
Zundamon: "Both 5 <= 10 and 5 <= 5 return true?"
Shikoku Metan: "Exactly. The feature is that it includes the equal case."
Zundamon: "It's commonly used for maximum value checks!"
Shikoku Metan: "It's useful for upper limit checks like score caps and inventory verification."
Zundamon: "Understanding the difference between < and <= is important!"

---

## 📺 Code for Display

```typescript
/** Example 1: Basic usage */
console.log(5 <= 10);   // true
console.log(5 <= 5);    // true
console.log(10 <= 5);   // false

/** Example 2: Type-safe comparison function */
function isLessOrEqual(a: number, b: number): boolean {
  return a <= b;
}

/** Example 3: Maximum value check */
const score: number = 100;
if (score <= 100) {
  console.log('Valid score');
}
```
