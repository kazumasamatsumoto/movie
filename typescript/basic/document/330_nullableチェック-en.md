# #330 "Nullable Checks"

Shikoku Metan: "Let's learn about nullable checks!"
Zundamon: "We can check for null with the strict equality operator!"
Shikoku Metan: "Yes. With if (user === null), we can determine if it's null."
Zundamon: "We can use type guard functions too, right?"
Shikoku Metan: "Exactly. With the isNotNull function, we can narrow down the type when it's not null."
Zundamon: "The Nullish Coalescing operator is convenient too!"
Shikoku Metan: "Yes. Using ??, we can concisely specify a default value for null cases."
Zundamon: "With proper null checks, we can write safe code!"

---

## 📺 Code for Display

```typescript
/** Example 1: Strict equality operator */
if (user === null) {
  return "No user";
}
console.log(user.name); // User type

/** Example 2: Type guard */
function isNotNull<T>(value: T | null): value is T {
  return value !== null;
}
if (isNotNull(user)) {
  user.name; // T type
}

/** Example 3: Nullish Coalescing */
const name = user ?? createGuestUser();
const port = config ?? 3000;
```
