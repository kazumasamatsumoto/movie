# #292 "Null and Empty String"

Shikoku Metan「Let's learn about the differences between null and empty string!」
Zundamon「'' and null look the same, don't they?」
Shikoku Metan「No. null is null type, '' is string type - they have different types.」
Zundamon「null === '' is false!」
Shikoku Metan「Exactly. They behave differently with Nullish Coalescing too.」
Zundamon「Empty string doesn't get replaced by ?? because it's a valid string?」
Shikoku Metan「Yes. null ?? "Guest" is "Guest", but "" ?? "Guest" is "".」
Zundamon「It's important to handle them type-safely with Union types!」

---

## 📺 Code for Display

```typescript
/** Example 1: Type differences */
let a: null = null;     // null type
let b: string = "";     // string type
null === "";  // false

/** Example 2: Nullish Coalescing behavior */
const name1 = null ?? "Guest";  // "Guest"
const name2 = "" ?? "Guest";    // "" (empty string is a valid value)

/** Example 3: Type safety */
// let str: string = null;  // Error
let str: string | null = null;  // OK
```
