# #331 "Optional Chaining - x?.property"

Shikoku Metan: "Let's learn about Optional Chaining!"
Zundamon: "We can safely access properties with the ?. operator!"
Shikoku Metan: "Yes. With user?.name, even if user is null or undefined, it won't throw an error and returns undefined."
Zundamon: "Can we use it for nested properties too?"
Shikoku Metan: "Exactly. Like user?.address?.city, we can safely access deep hierarchies."
Zundamon: "We can use it for array elements and method calls too!"
Shikoku Metan: "Yes. Like array?.[0] or obj?.method?.(), we can utilize it in various situations."
Zundamon: "With Optional Chaining, we can write safer code!"

---

## 📺 Code for Display

```typescript
/** Example 1: Basic usage */
const user: User | null = getUser();
const name = user?.name; // string | undefined
const email = user?.email;

/** Example 2: Nested properties */
const city = user?.address?.city;
const zip = user?.address?.zipCode ?? "N/A";

/** Example 3: Arrays and methods */
const firstItem = array?.[0];
const result = obj?.method?.();
```
