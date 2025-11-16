# #354 "Nullish Check - x != null"

Shikoku Metan: "value != null is a handy nullish check!"
Zundamon: "It detects both null and undefined at once?"
Shikoku Metan: "Yes, inside the block the type becomes non-nullish."
Zundamon: "That's far shorter than writing two strict comparisons!"
Shikoku Metan: "And TypeScript narrows the type to string or number immediately."
Zundamon: "So after data != null I can safely do arithmetic?"
Shikoku Metan: "Exactly; doubled = data * 2 no longer raises errors."
Zundamon: "I'll rely on concise nullish checks to protect my logic!"

---

## 📺 Code for Display

```typescript
/** Example 1: Basic nullish check */
function process(value: string | null | undefined) {
  if (value != null) {
    // value: string
    console.log(value.toUpperCase());
  }
}

/** Example 2: Difference from strict equality */
if (value !== null && value !== undefined) {
  // Verbose
}
if (value != null) {
  // Concise and recommended
}

/** Example 3: Acting as a type guard */
const data: number | null | undefined = getData();
if (data != null) {
  const doubled = data * 2;  // Treated as number
}
```
