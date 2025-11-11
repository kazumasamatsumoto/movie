# #343 "Optional Property - prop?"

Shikoku Metan「Let's learn about optional properties!」
Zundamon「We add a ? after the property name!」
Shikoku Metan「Yes. That makes the property optional.」
Zundamon「Can we omit them in object literals?」
Shikoku Metan「Exactly. We only need to specify required properties, optionals can be omitted.」
Zundamon「We can use it in type aliases too!」
Shikoku Metan「Yes. It's suitable for properties that assume default values.」
Zundamon「With optional properties, we can create flexible interfaces!」

---

## 📺 Code for Display

```typescript
/** Example 1: Basics of optional properties */
interface User {
  name: string;
  age?: number;       // Optional
  email?: string;     // Optional
}

/** Example 2: Omitting in object literals */
const user1: User = { name: "Alice", age: 30 };
const user2: User = { name: "Bob" }; // age and email are omitted

/** Example 3: Using in type aliases */
type Config = {
  host: string;
  port?: number;      // Assumes a default value
  ssl?: boolean;
};
```
