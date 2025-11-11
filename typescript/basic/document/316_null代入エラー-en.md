# #316 "null Assignment Error"

Shikoku Metan: "Let's learn about null assignment errors with strictNullChecks!"
Zundamon: "Assigning null to a string type causes an error!"
Shikoku Metan: "That's right. With strictNullChecks enabled, null must be explicitly allowed."
Zundamon: "The first fix method is using a Union type like string | null, right?"
Shikoku Metan: "Exactly. Including null in the type allows the assignment."
Zundamon: "Non-Null Assertion can also be used, but it's not recommended?"
Shikoku Metan: "Yes. It bypasses type checking, creating runtime error risks."
Zundamon: "Explicitly handling null with Union types is more type-safe!"

---

## 📺 Code for Display

```typescript
/** Example 1: Error with strictNullChecks enabled */
// strictNullChecks: true
let name: string = null; // エラー
// Type 'null' is not assignable to type 'string'

/** Example 2: Fix method 1 - Union type */
let name: string | null = null; // OK
name = "Alice"; // OK

/** Example 3: Fix method 2 - Non-Null Assertion (not recommended) */
let name: string = null!; // OK (型チェック回避)
// 実行時エラーのリスクあり
```
