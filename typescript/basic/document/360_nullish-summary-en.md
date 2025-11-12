# #360 "Nullish Type Summary"

Shikoku Metan: "Let's wrap up the nullish type chapter."
Zundamon: "We define it with type Nullish<T> = T | null | undefined, right?"
Shikoku Metan: "Yes, perfect for values like getValue() that might be absent."
Zundamon: "When using them, I combine user?.name ?? 'Guest'?"
Shikoku Metan: "Exactly; mixing ??, ?. and != null keeps operations safe."
Zundamon: "Even config objects such as env?.HOST ?? 'localhost' benefit?"
Shikoku Metan: "They do, and response?.data ?? [] gracefully handles missing arrays."
Zundamon: "Understanding nullish types lets us write trustworthy code!"

---

## 📺 Code for Display

```typescript
/** Example 1: Defining the nullish type */
type Nullish<T> = T | null | undefined;
const value: string | null | undefined = getValue();

/** Example 2: Safe operations */
const displayName = user?.name ?? "Guest";
const age = user?.age ?? 0;
if (value != null) {
  console.log(value);
}

/** Example 3: Practical pattern */
const config = {
  host: env?.HOST ?? "localhost",
  port: env?.PORT ?? 8080,
  data: response?.data ?? [],
};
```
