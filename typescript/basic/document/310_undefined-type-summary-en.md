# #310 "undefined Type Summary"

Shikoku Metan: "Let's summarize the undefined type!"
Zundamon: "The undefined type is an important type representing the absence of values!"
Shikoku Metan: "That's right. It's frequently used in union types and optional properties."
Zundamon: "For undefined checks, !== undefined and the nullish coalescing operator ?? are convenient, right?"
Shikoku Metan: "Exactly. Type guards allow us to handle values safely."
Zundamon: "With the Option type pattern, error handling can be type-safe too!"
Shikoku Metan: "It's also important to understand the difference from void type and JSON conversion behavior."
Zundamon: "By using the undefined type correctly, we can write code with fewer bugs!"

---

## 📺 Code for Display

```typescript
/** Example 1: undefined type basics */
let value: string | undefined;
interface User {
  name: string;
  age?: number;  // optional
}

/** Example 2: undefined checks */
if (value !== undefined) {
  value.toUpperCase(); // string type
}
const name = userName ?? "Guest";

/** Example 3: Practical patterns */
function greet(name?: string): void {
  console.log(name ?? "Guest");
}
type Option<T> = T | undefined;
```
