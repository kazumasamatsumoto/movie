# #304 "undefined Checks"

Shikoku Metan「Let's learn about undefined checks!」
Zundamon「How do we check if something is undefined?」
Shikoku Metan「Yes. We can use strict equality === as a type guard.」
Zundamon「We check with value === undefined!」
Shikoku Metan「Exactly. The Nullish Coalescing operator is also convenient.」
Zundamon「What does the ?? operator do?」
Shikoku Metan「Yes. It uses the default value only when undefined/null.」
Zundamon「Combining with optional chaining ?. makes it safe to handle!」

---

## 📺 Code for Display

```typescript
/** Example 1: Strict equality and type guard */
if (value === undefined) {
  console.log("undefined");
}
function isDefined<T>(value: T | undefined): value is T {
  return value !== undefined;
}

/** Example 2: Nullish Coalescing */
const name = userName ?? "Guest";
const config = settings?.timeout ?? 5000;

/** Example 3: Optional chaining */
const zip = user?.address?.zipCode;
// undefined if user or address is undefined
```
