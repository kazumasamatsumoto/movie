# #347 "Undefinedable Checks"

Shikoku Metan: "Let's learn how to check undefinedable values!"
Zundamon: "We compare with undefined using the strict equality operator!"
Shikoku Metan: "Yes. value !== undefined works as a type guard."
Zundamon: "Can we also check with the typeof operator?"
Shikoku Metan: "Exactly. With typeof value === "string", we can narrow down to string type."
Zundamon: "Can we use Optional Chaining too?"
Shikoku Metan: "Yes. We can safely access properties like value?.length."
Zundamon: "Let's write safe code with proper checks!"

---

## 📺 Code for Display

```typescript
/** Example 1: Basic check */
function process(value: string | undefined) {
  if (value !== undefined) {
    console.log(value.toUpperCase());
  }
}

/** Example 2: Check with typeof operator */
if (typeof value === "string") {
  console.log(value.length);
}

/** Example 3: Optional Chaining and default value */
const length = value?.length ?? 0;
const upper = value?.toUpperCase();
```
