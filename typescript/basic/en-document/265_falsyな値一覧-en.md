# #265 "List of Falsy Values"

Shikoku Metan「Let's learn about the list of falsy values!」
Zundamon「How many are there in total?」
Shikoku Metan「Yes. There are only six falsy values in JavaScript.」
Zundamon「false, 0, empty string, null, undefined, and NaN!」
Shikoku Metan「Exactly. All other values besides these are truthy.」
Zundamon「Are there any values to be careful about?」
Shikoku Metan「Yes. '0', [], and {} may look falsy, but they're actually truthy.」
Zundamon「Just remember these six and you're perfect!」

---

## 📺 Code for Display

```typescript
/** Example 1: List of falsy values (all 6) */
console.log(Boolean(false));     // false
console.log(Boolean(0));         // false
console.log(Boolean(''));        // false
console.log(Boolean(null));      // false
console.log(Boolean(undefined)); // false
console.log(Boolean(NaN));       // false

/** Example 2: Note: These are truthy */
console.log(Boolean('0'));       // true (string)
console.log(Boolean([]));        // true (empty array)
console.log(Boolean({}));        // true (empty object)
```
