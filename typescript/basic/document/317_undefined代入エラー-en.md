# #317 "undefined Assignment Error"

Shikoku Metan: "Let's learn about undefined assignment errors with strictNullChecks!"
Zundamon: "Assigning undefined to a string type causes an error!"
Shikoku Metan: "That's right. With strictNullChecks enabled, undefined must also be explicitly allowed."
Zundamon: "The first fix method is using a Union type like string | undefined, right?"
Shikoku Metan: "Exactly. Including undefined in the type allows the assignment."
Zundamon: "The second fix method with optional seems convenient too!"
Shikoku Metan: "Yes. Adding ? to properties or parameters makes them string | undefined."
Zundamon: "Explicitly handling undefined with types is safer!"

---

## 📺 Code for Display

```typescript
/** Example 1: Error with strictNullChecks enabled */
// strictNullChecks: true
let name: string = undefined; // エラー
// Type 'undefined' is not assignable to type 'string'

/** Example 2: Fix method 1 - Union type */
let name: string | undefined = undefined; // OK
name = "Alice"; // OK

/** Example 3: Fix method 2 - Optional */
interface User {
  name?: string; // string | undefined
}
function greet(name?: string) {}
```
