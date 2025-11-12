# #366 "Mistake (1) - Confusion"

Shikoku Metan: "Because it shares the same symbol, the ! operator is often confused with logical NOT."
Zundamon: "So const result1 = !value and value! do totally different things, huh?"
Shikoku Metan: "Exactly—the former flips a boolean while the latter removes nullish types."
Zundamon: "Writing something like if (!user!) would be nonsense?"
Shikoku Metan: "Yes, it becomes unreadable and may even be a syntax error."
Zundamon: "When I need clarity I should compare explicitly with user === null?"
Shikoku Metan: "Right, and for truthy checks just evaluate user alone without the assertion."
Zundamon: "Keeping their roles separate helps me avoid typos!"

---

## 📺 Code for Display

```typescript
/** Example 1: Easy-to-confuse example */
const value: boolean | null = getValue();
const result1 = !value;   // Logical NOT
const result2 = value!;   // Non-null Assertion

/** Example 2: Incorrect usage */
if (!user!) {  // Confusing
  // ...
}

/** Example 3: Clear comparisons */
if (user === null) {  // Explicit
  // ...
}
if (!user) {  // Truthy check
  // ...
}
```
