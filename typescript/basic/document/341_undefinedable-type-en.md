# #341 "Undefinedable Type - T | undefined"

Shikoku Metan「Let's learn about undefinedable types!」
Zundamon「With T | undefined, we can create types that allow undefined!」
Shikoku Metan「Yes. We can explicitly express cases where values don't exist.」
Zundamon「What's the relationship with optional properties?」
Shikoku Metan「Exactly. property?: T means the same as property: T | undefined.」
Zundamon「Can we use it for function arguments too?」
Shikoku Metan「Yes. By performing undefined checks, we can handle values safely.」
Zundamon「With undefinedable types, we can explicitly handle the absence of values!」

---

## 📺 Code for Display

```typescript
/** Example 1: Basics of undefinedable type */
type Undefinedable<T> = T | undefined;
let name: string | undefined;
name = "Alice";
name = undefined;

/** Example 2: Using in function arguments */
function greet(name: string | undefined) {
  if (name !== undefined) {
    console.log(`Hello, ${name}`);
  }
}

/** Example 3: Relationship with optional */
interface User {
  name: string;
  age: number | undefined;  // Explicit undefinedable
  email?: string;           // Optional (= string | undefined)
}
```
