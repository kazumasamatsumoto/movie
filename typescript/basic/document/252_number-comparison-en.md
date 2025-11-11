# #252 "Number Comparison"

Shikoku Metan: "Let's learn about number comparison!"
Zundamon: "Integer comparison is easy, right!"
Shikoku Metan: "Yes. However, we need to be careful with floating-point numbers."
Zundamon: "I've heard that 0.1 + 0.2 === 0.3 returns false!"
Shikoku Metan: "That's correct. Errors occur due to floating-point precision issues."
Zundamon: "How do we solve this?"
Shikoku Metan: "We create a comparison function using epsilon (tolerance)."
Zundamon: "Calculate the difference with Math.abs and allow tiny errors!"

---

## 📺 Code for Display

```typescript
/** Example 1: Integer comparison */
console.log(10 > 5);    // true
console.log(10 === 10); // true

/** Example 2: Floating-point problem */
console.log(0.1 + 0.2 === 0.3); // false

/** Example 3: Comparison with tolerance */
function isClose(a: number, b: number, epsilon = 1e-10): boolean {
  return Math.abs(a - b) < epsilon;
}

console.log(isClose(0.1 + 0.2, 0.3)); // true
```
