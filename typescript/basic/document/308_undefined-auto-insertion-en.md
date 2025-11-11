# #308 "Automatic Insertion of undefined"

Shikoku Metan: "Let's learn about automatic insertion of undefined!"
Zundamon: "When optional parameters are omitted, they automatically become undefined!"
Shikoku Metan: "That's right. When arguments aren't passed to a function, their values are treated as undefined."
Zundamon: "Functions without return statements also implicitly return undefined, right?"
Shikoku Metan: "Exactly. If there's no explicit return, undefined is returned."
Zundamon: "Optional properties are also automatically undefined when omitted!"
Shikoku Metan: "TypeScript has many situations where undefined is auto-inserted, so understanding this is important."
Zundamon: "Using the nullish coalescing operator ?? to set default values is safe!"

---

## 📺 Code for Display

```typescript
/** Example 1: Optional parameters */
function greet(name?: string) {
  console.log(name ?? "Guest"); // name can be undefined
}
greet(); // name = undefined

/** Example 2: Implicit return */
function noReturn() {
  // no return statement
}
const result = noReturn(); // undefined

/** Example 3: Optional properties */
interface User {
  name: string;
  age?: number;  // undefined when omitted
}
const user: User = { name: "Alice" };
// user.age is undefined
```
