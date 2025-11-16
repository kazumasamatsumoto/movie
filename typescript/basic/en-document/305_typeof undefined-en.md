# #305 "typeof undefined"

Shikoku Metan「Let's learn about typeof undefined!」
Zundamon「What happens when we check undefined with typeof operator?」
Shikoku Metan「Yes. It returns the string "undefined".」
Zundamon「Different from typeof null which is "object"!」
Shikoku Metan「Exactly. We can also check with typeof operator.」
Zundamon「We check with typeof value === "undefined"?」
Shikoku Metan「Yes. It's safe even for undeclared variables without errors.」
Zundamon「Direct === causes ReferenceError, but typeof is safe!」

---

## 📺 Code for Display

```typescript
/** Example 1: typeof undefined */
typeof undefined; // "undefined"
typeof null;      // "object"

/** Example 2: Check with typeof */
if (typeof value === "undefined") {
  console.log("undefined");
}

/** Example 3: Safe for undeclared variables */
typeof undeclaredVar === "undefined"; // true (no error)
undeclaredVar === undefined; // ReferenceError
```
