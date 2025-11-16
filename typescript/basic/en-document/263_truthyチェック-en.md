# #263 "Truthy Check"

Shikoku Metan「Let's learn about truthy checks!」
Zundamon「It's a way to check if a value exists!」
Shikoku Metan「Yes. Directly evaluating a value in an if statement checks if it's truthy.」
Zundamon「What kinds of values are truthy?」
Shikoku Metan「Exactly. Non-zero numbers, non-empty strings, arrays, objects, and so on.」
Zundamon「Can I check with the Boolean function?」
Shikoku Metan「Yes. Using Boolean() lets you check if any value is truthy or falsy.」
Zundamon「It's convenient for checking value existence!」

---

## 📺 Code for Display

```typescript
/** Example 1: Truthy check */
function process(value: string | number | null) {
  if (value) {
    // When the value is truthy
    console.log('Value exists');
  }
}

/** Example 2: Examples of truthy values */
console.log(Boolean(1));        // true
console.log(Boolean('hello'));  // true
console.log(Boolean([]));       // true
console.log(Boolean({}));       // true
console.log(Boolean(true));     // true
```
