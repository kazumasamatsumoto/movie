# #303 "The undefined Type"

Shikoku Metan「Let's learn about the undefined type!」
Zundamon「Can we use undefined as a type?」
Shikoku Metan「Yes. There's an undefined type that only accepts the undefined literal.」
Zundamon「typeof undefined returns the string "undefined"!」
Shikoku Metan「Exactly. strictNullChecks increases type safety.」
Zundamon「What happens when this option is enabled?」
Shikoku Metan「Yes. Assigning undefined to string causes an error.」
Zundamon「NonNullable<T> can exclude undefined from types!」

---

## 📺 Code for Display

```typescript
/** Example 1: undefined type */
let value: undefined = undefined;
type UndefinedType = undefined;
typeof undefined; // "undefined"

/** Example 2: strictNullChecks: true */
let str: string = undefined;  // Error
let str: string | undefined = undefined;  // OK

/** Example 3: Exclude with NonNullable<T> */
type Result = string | number | undefined;
type NonUndef = NonNullable<Result>;
// → string | number
```
