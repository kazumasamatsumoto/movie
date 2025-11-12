# #355 "Nullish Coalescing - ??"

Shikoku Metan: "Let's focus on the Nullish Coalescing operator ??."
Zundamon: "It only replaces null or undefined with defaults, right?"
Shikoku Metan: "Yes, expressions like null ?? 'default' or undefined ?? 'default' are the basics."
Zundamon: "So function arguments can fall back to 'Guest' with name ?? 'Guest'?"
Shikoku Metan: "Exactly. It's very readable in greet-like helpers."
Zundamon: "Configuration objects can use port ?? 8080 as well?"
Shikoku Metan: "Right, and it works even on nested options?.timeout ?? 3000."
Zundamon: "I'll use ?? to fill in values only when they're truly nullish!"

---

## 📺 Code for Display

```typescript
/** Example 1: Nullish Coalescing basics */
const value1 = null ?? "default";      // "default"
const value2 = undefined ?? "default"; // "default"
const value3 = "hello" ?? "default";   // "hello"

/** Example 2: Using it inside a function */
function greet(name: string | null | undefined) {
  const displayName = name ?? "Guest";
  console.log(`Hello, ${displayName}`);
}

/** Example 3: Defaulting configuration values */
const config = {
  port: options?.port ?? 8080,
  timeout: options?.timeout ?? 3000,
  retries: options?.retries ?? 3,
};
```
