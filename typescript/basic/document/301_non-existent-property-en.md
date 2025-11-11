# #301 "Non-existent Properties"

Shikoku Metan「Let's learn about non-existent properties!」
Zundamon「What happens when we access undefined properties?」
Shikoku Metan「Yes. TypeScript gives a compile error.」
Zundamon「user.age errors when age isn't defined!」
Shikoku Metan「Exactly. We can safely access with optional chaining.」
Zundamon「Using ?. returns undefined?」
Shikoku Metan「Yes. We can chain like user?.profile?.age.」
Zundamon「Writing age?: number in type definitions makes it safe to handle!」

---

## 📺 Code for Display

```typescript
/** Example 1: Non-existent property */
const user = { name: "Alice" };
// user.age;  // Error: Property 'age' does not exist

/** Example 2: Optional chaining */
const age = user?.profile?.age;
// undefined if profile doesn't exist

/** Example 3: Safe with type definition */
interface User {
  name: string;
  age?: number;  // Optional
}
const user: User = { name: "Alice" };
user.age;  // number | undefined
```
