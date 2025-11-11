# #247 "Greater Than Operator Types"

Shikoku Metan: "Let's learn about the types that can be used with the greater than operator!"
Zundamon: "Can we compare various types, not just numbers?"
Shikoku Metan: "Yes. It works with comparable types like numbers, strings, and Date objects."
Zundamon: "Strings are compared in dictionary order, right!"
Shikoku Metan: "Exactly. 'b' > 'a' returns true."
Zundamon: "Being able to compare Date objects is convenient!"
Shikoku Metan: "It's commonly used when determining which date is newer or older."
Zundamon: "It's important to understand that comparison rules differ by type!"

---

## 📺 Code for Display

```typescript
/** Example 1: Numeric comparison */
const num1: number = 10;
const num2: number = 5;
console.log(num1 > num2); // true

/** Example 2: String comparison (dictionary order) */
const str1: string = 'b';
const str2: string = 'a';
console.log(str1 > str2); // true

/** Example 3: Date type comparison */
const date1: Date = new Date('2024-01-02');
const date2: Date = new Date('2024-01-01');
console.log(date1 > date2); // true
```
