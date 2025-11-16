# #296 "Undefined Type"

Shikoku Metan「Let's learn about the undefined type!」
Zundamon「When do we use undefined?」
Shikoku Metan「Yes. It's a type that represents an undefined value.」
Zundamon「Is it related to optional properties?」
Shikoku Metan「Exactly. name?: string means the same as string | undefined.」
Zundamon「Does it error when strictNullChecks is enabled?」
Shikoku Metan「Yes. undefined cannot be assigned to number type.」
Zundamon「Explicitly handling undefined with Union types is safe!」

---

## 📺 Code for Display

```typescript
/** Example 1: undefined type basics */
let value: undefined = undefined;
let name: string | undefined;

/** Example 2: Optional properties */
interface User {
  name?: string;  // string | undefined
  age?: number;   // number | undefined
}

/** Example 3: With strictNullChecks enabled */
// let id: number = undefined; // Error
let id: number | undefined = undefined; // OK
```
