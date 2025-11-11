# #251 "String Comparison"

Shikoku Metan: "Let's learn about string comparison!"
Zundamon: "Can strings be compared using comparison operators?"
Shikoku Metan: "Yes. Strings are compared in dictionary order (Unicode order)."
Zundamon: "'apple' < 'banana' returns true, right!"
Shikoku Metan: "Exactly. Between uppercase and lowercase, uppercase is considered smaller."
Zundamon: "'A' < 'a' also returns true?"
Shikoku Metan: "Yes. Strings of different lengths can be compared, and 'abc' < 'abcd' is true."
Zundamon: "Creating type-safe string comparison functions makes it even more convenient!"

---

## 📺 Code for Display

```typescript
/** Example 1: Dictionary order comparison */
console.log('apple' < 'banana'); // true
console.log('cat' > 'dog');      // false

/** Example 2: Uppercase and lowercase */
console.log('A' < 'a');  // true
console.log('Z' < 'a');  // true

/** Example 3: Type-safe string comparison */
function compareStrings(a: string, b: string): number {
  return a === b ? 0 : a < b ? -1 : 1;
}
```
