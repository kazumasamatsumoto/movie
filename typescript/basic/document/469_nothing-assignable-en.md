# #469 "Nothing Assignable"

Shikoku Metan: "Absolutely nothing assigns to never."
Zundamon: "value: never rejected numbers and undefined."
Shikoku Metan: "Only expressions already typed as never can be stored."
Zundamon: "We assigned fail() to const result: never."
Shikoku Metan: "Exhaustive checks cast remaining cases to never."

---

## 📺 Code for Display

```typescript
/** Example 1: Non-assignable */
let value: never;

/** Example 2: Assigning from never function */
function fail(): never {
  throw new Error("Failed");
}
const result: never = fail();

/** Example 3: Exhaustive check */
function check(value: string | number): string {
  if (typeof value === "string") {
    return value;
  } else if (typeof value === "number") {
    return value.toString();
  }
  const exhaustive: never = value;
  return exhaustive;
}
```
