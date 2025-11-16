# #313 "Behavior When Enabled"

Shikoku Metan「Let's learn about the behavior when strictNullChecks is enabled!」
Zundamon「What happens when it's enabled?」
Shikoku Metan「Yes. To assign null or undefined, you need to explicitly specify it with a Union type.」
Zundamon「You get an error unless you write it like string | null!」
Shikoku Metan「Exactly. Null checks become mandatory, allowing you to write safe code.」
Zundamon「When you do a null check with an if statement, the type is narrowed?」
Shikoku Metan「Yes. Through Type Narrowing, after the check it's treated as a non-null type.」
Zundamon「Optional properties become number | undefined!」

---

## 📺 Code for Display

```typescript
/** Example 1: Explicitly specify with Union type */
// strictNullChecks: true
let name: string = null; // Error
let name: string | null = null; // OK

/** Example 2: Null checks are mandatory */
function greet(name: string | null) {
  if (name !== null) {
    return name.toUpperCase(); // Safe
  }
  return "Guest";
}

/** Example 3: Optional properties */
interface User {
  name: string;
  age?: number; // number | undefined
}
```
