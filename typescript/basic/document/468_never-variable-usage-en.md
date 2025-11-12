# #468 "Never Variables"

Shikoku Metan: "Variables of type never accept no assignments."
Zundamon: "neverValue = 1; was invalid."
Shikoku Metan: "Conditional types use never to remove null or undefined."
Zundamon: "NonNullable and Exclude demonstrated that."
Shikoku Metan: "Use never to prune union members."

---

## 📺 Code for Display

```typescript
/** Example 1: Never variable */
let neverValue: never;

/** Example 2: NonNullable */
type NonNullable<T> = T extends null | undefined ? never : T;
type Result = NonNullable<string | null>;

/** Example 3: Exclude */
type Exclude<T, U> = T extends U ? never : T;
type Numbers = Exclude<string | number, string>;
```
