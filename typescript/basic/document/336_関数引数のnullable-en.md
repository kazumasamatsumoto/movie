# #336 "Nullable Function Parameters"

Shikoku Metan: "Let's learn about nullable function parameters!"
Zundamon: "We can use nullable types for function parameters!"
Shikoku Metan: "Yes. With User | null type parameters, we can define functions that accept null."
Zundamon: "Is it different from optional parameters?"
Shikoku Metan: "Exactly. Nullable parameters require explicitly passing null."
Zundamon: "We can combine them with default values too!"
Shikoku Metan: "Yes. We can specify null as the default value for parameters."
Zundamon: "With nullable parameters, we can create flexible functions!"

---

## 📺 Code for Display

```typescript
/** Example 1: nullable parameter */
function greet(user: User | null): string {
  if (user === null) {
    return "Hello, Guest";
  }
  return `Hello, ${user.name}`;
}

/** Example 2: Difference from optional */
function process1(data: string | null) {
  // Need to explicitly pass null
}
function process2(data?: string) {
  // Can be omitted
}

/** Example 3: Combining with default values */
function log(message: string | null = null) {
  console.log(message ?? "No message");
}
```
