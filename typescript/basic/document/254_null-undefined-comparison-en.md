# #254 "Null/Undefined Comparison"

Shikoku Metan: "Let's learn about null and undefined comparison!"
Zundamon: "These two are similar but different, right?"
Shikoku Metan: "Yes. They're considered equal with ==, but different with ===."
Zundamon: "Does null == undefined return true?"
Shikoku Metan: "Exactly. However, null === undefined returns false."
Zundamon: "We should use === when we want strict comparison!"
Shikoku Metan: "Yes. Using type predicate functions makes it even more type-safe."
Zundamon: "Explicitly checking with isNull or isUndefined functions is better!"

---

## 📺 Code for Display

```typescript
/** Example 1: Comparison with == (type coercion) */
console.log(null == undefined);  // true

/** Example 2: Comparison with === (strict) */
console.log(null === undefined); // false
console.log(null === null);      // true
console.log(undefined === undefined); // true

/** Example 3: Type-safe checks */
function isNull(value: unknown): value is null {
  return value === null;
}

function isUndefined(value: unknown): value is undefined {
  return value === undefined;
}
```
