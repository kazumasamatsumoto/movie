# #348 "Using Optional Chaining"

Shikoku Metan: "Let's learn how to use Optional Chaining!"
Zundamon: "We can safely access properties with ?.!"
Shikoku Metan: "Yes. Like user.name?.toUpperCase(), it's safe even when undefined."
Zundamon: "Can we use it for method calls too?"
Shikoku Metan: "Exactly. With callback?.(), we can safely call functions even when undefined."
Zundamon: "Can we do nested access too?"
Shikoku Metan: "Yes. We can use it for deep hierarchies like user?.address?.city."
Zundamon: "Let's write concise code with Optional Chaining!"

---

## 📺 Code for Display

```typescript
/** Example 1: Property access */
const user: { name?: string } = {};
const name = user.name?.toUpperCase();
const length = user.name?.length;

/** Example 2: Method call */
const callback: (() => void) | undefined = getCallback();
callback?.();

/** Example 3: Nested access with default value */
const city = user?.address?.city ?? "Unknown";
const phone = user?.contact?.phone?.trim();
```
