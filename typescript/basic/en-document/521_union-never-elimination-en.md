# #521 "Union Types Drop Never"

Shikoku Metan: "Whenever you add never to a union it vanishes."
Zundamon: "That's why string | never simplifies to string."
Shikoku Metan: "NonNullable<T> turns null/undefined into never and strips them away."
Zundamon: "Even boolean | null | undefined collapses to just boolean."
Shikoku Metan: "Adding never multiple times still yields the same union."
Zundamon: "The Complex example shrank to string | number | boolean."
Shikoku Metan: "Knowing this makes type-level arithmetic easier to read."
Zundamon: "Remember: useless never members disappear by design."

---

## 📺 Code for Display

```typescript
/** Example 1: Never disappears from unions */
type A = string | never;        // string
type B = number | never;        // number
type C = boolean | never;       // boolean
type D = string | number | never;  // string | number
```

```typescript
/** Example 2: Using NonNullable */
type NonNullable<T> = T extends null | undefined ? never : T;

type CleanString = NonNullable<string | null>;  // string
type CleanNumber = NonNullable<number | undefined>;  // number
type CleanBool = NonNullable<boolean | null | undefined>;  // boolean
```

```typescript
/** Example 3: Multiple never entries still vanish */
type Complex =
  | string
  | never
  | number
  | never
  | boolean;  // string | number | boolean
```
