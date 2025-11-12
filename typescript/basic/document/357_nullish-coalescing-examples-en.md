# #357 "Examples of ??"

Shikoku Metan: "Let's examine practical ?? patterns."
Zundamon: "We can configure host and port from environment variables?"
Shikoku Metan: "Yes, env.HOST ?? 'localhost' keeps the code concise."
Zundamon: "Does it pair well with Optional Chaining?"
Shikoku Metan: "Absolutely. user?.address?.city ?? 'Unknown' fills gaps cleanly."
Zundamon: "Can we also default function arguments like age?"
Shikoku Metan: "Sure, age ?? 0 only substitutes when the value is nullish."
Zundamon: "I'll standardize settings with reusable ?? patterns!"

---

## 📺 Code for Display

```typescript
/** Example 1: Defaulting configuration */
const config = {
  host: env.HOST ?? "localhost",
  port: env.PORT ?? 8080,
  timeout: env.TIMEOUT ?? 3000,
};

/** Example 2: Combining with Optional Chaining */
const userName = user?.name ?? "Anonymous";
const city = user?.address?.city ?? "Unknown";
const email = user?.contacts?.[0]?.email ?? "no-email";

/** Example 3: Using it in function arguments */
function createUser(name: string, age?: number | null) {
  return {
    name,
    age: age ?? 0,
    status: "active",
  };
}
```
