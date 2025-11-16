# #332 "Nullish Coalescing - x ?? default"

Shikoku Metan: "Let's learn about the Nullish Coalescing operator!"
Zundamon: "We can set default values with the ?? operator!"
Shikoku Metan: "Yes. With userName ?? "Guest", we use the default value only when userName is null or undefined."
Zundamon: "Is it different from the || operator?"
Shikoku Metan: "Exactly. || treats 0 and empty strings as falsy too, but ?? only targets null and undefined."
Zundamon: "We can combine it with Optional Chaining!"
Shikoku Metan: "Yes. Like user?.age ?? 18, we can achieve both safe access and default values."
Zundamon: "With Nullish Coalescing, we can write more flexible code!"

---

## 📺 Code for Display

```typescript
/** Example 1: Basic usage */
const name = userName ?? "Guest";
const port = config.port ?? 3000;

/** Example 2: Difference from || */
const count1 = 0 || 10;  // 10 (0 is falsy)
const count2 = 0 ?? 10;  // 0  (0 is a valid value)

/** Example 3: Combined with Optional Chaining */
const city = user?.address?.city ?? "Unknown";
const age = user?.age ?? 18;
```
