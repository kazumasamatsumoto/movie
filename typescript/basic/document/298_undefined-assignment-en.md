# #298 "Undefined Assignment"

Shikoku Metan「Let's learn about undefined assignment!」
Zundamon「What values can we assign?」
Shikoku Metan「Yes. We can assign undefined or normal values to Union type variables.」
Zundamon「string | undefined can hold either one!」
Shikoku Metan「Exactly. We can handle values flexibly.」
Zundamon「What about errors with strictNullChecks?」
Shikoku Metan「undefined cannot be assigned to number type, so Union types are needed.」
Zundamon「Optional properties can also be omitted!」

---

## 📺 Code for Display

```typescript
/** Example 1: Assigning undefined */
let name: string | undefined = undefined;
name = "Alice";  // OK
name = undefined; // OK

/** Example 2: With strictNullChecks enabled */
// let id: number = undefined;  // Error
let id: number | undefined = undefined;  // OK

/** Example 3: Optional properties */
const user: User = {
  name: "Alice",
  age: undefined  // Optional, can be omitted
};
```
