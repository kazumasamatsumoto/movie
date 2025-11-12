# #363 "Meaning of the ! Operator"

Shikoku Metan: "The ! operator removes nullish types at the type level."
Zundamon: "So the type becomes value!: string, right?"
Shikoku Metan: "Yes, it only affects TypeScript and leaves no trace in JavaScript."
Zundamon: "Meaning that after transpilation it's just a normal access?"
Shikoku Metan: "Exactly—value!.length becomes value.length."
Zundamon: "Can I collapse number | null | undefined down to number the same way?"
Shikoku Metan: "Yes, writing data! * 2 treats it as number immediately."
Zundamon: "So it's purely a type conversion with zero runtime safety!"

---

## 📺 Code for Display

```typescript
/** Example 1: Type conversion */
const value: string | null = getValue();
// value!: string (null removed)
const upper = value!.toUpperCase();

/** Example 2: Code after transpilation */
// TypeScript
const length = value!.length;
// JavaScript (after transpilation)
const length = value.length;

/** Example 3: Removing nullish combinations */
const data: number | null | undefined = getData();
const doubled = data! * 2;  // Treat as number
```
