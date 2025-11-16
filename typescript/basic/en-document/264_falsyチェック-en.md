# #264 "Falsy Check"

Shikoku Metan「Let's learn about falsy checks!」
Zundamon「It's a way to check if a value doesn't exist!」
Shikoku Metan「Yes. Using ! to evaluate a value checks if it's falsy.」
Zundamon「What kinds of values are falsy?」
Shikoku Metan「Exactly. There are six: false, 0, empty string, null, undefined, and NaN.」
Zundamon「All of these become false!」
Shikoku Metan「Yes. Checking with Boolean() returns false for all of them.」
Zundamon「It's useful for error handling!」

---

## 📺 Code for Display

```typescript
/** Example 1: Falsy check */
function process(value: string | number | null) {
  if (!value) {
    // When the value is falsy
    console.log('Value does not exist or is a falsy value');
  }
}

/** Example 2: Examples of falsy values */
console.log(Boolean(false));    // false
console.log(Boolean(0));        // false
console.log(Boolean(''));       // false
console.log(Boolean(null));     // false
console.log(Boolean(undefined));// false
console.log(Boolean(NaN));      // false
```
