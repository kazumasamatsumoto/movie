# #471 "Type Hierarchy"

Shikoku Metan: "never sits at the very bottom of the type hierarchy."
Zundamon: "fail() could be assigned to string or number."
Shikoku Metan: "But nothing can be assigned back into never."
Zundamon: "Union types like string | never collapse to string?"
Shikoku Metan: "Exactly—never disappears there."
Zundamon: "Knowing this makes type behavior predictable."
Shikoku Metan: "Remember never means “no value at all.”"
Zundamon: "I will watch where never lives in the hierarchy!"

---

## 📺 Code for Display

```typescript
/** Example 1: never assigns to anything */
function fail(): never {
  throw new Error("Failed");
}
const str: string = fail();
const num: number = fail();
const bool: boolean = fail();

/** Example 2: Opposite assignment fails */
let value: never;
// value = "string";

/** Example 3: never in unions */
type Result = string | never;
type Empty = never | never;
```
