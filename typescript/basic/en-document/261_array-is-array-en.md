# #261 "Array.isArray()"

Shikoku Metan「Let's learn about Array.isArray()!」
Zundamon「It's a method to check if something is an array!」
Shikoku Metan「Yes. Since typeof returns object for arrays too, we need this method.」
Zundamon「Can we use it with types like string[] | string?」
Shikoku Metan「Exactly. For arrays use join(), for strings use toUpperCase().」
Zundamon「Do null and empty objects return false properly?」
Shikoku Metan「Yes. Only arrays return true, so we can make accurate checks.」
Zundamon「It's convenient for writing array-specific processing safely!」

---

## 📺 Code for Display

```typescript
/** Example 1: Basic usage */
function processValue(value: string[] | string) {
  if (Array.isArray(value)) {
    console.log(value.join(', '));
  } else {
    console.log(value.toUpperCase());
  }
}

/** Example 2: Array check */
console.log(Array.isArray([]));       // true
console.log(Array.isArray([1, 2]));   // true
console.log(Array.isArray('hello')); // false
console.log(Array.isArray({}));       // false
console.log(Array.isArray(null));     // false
```
