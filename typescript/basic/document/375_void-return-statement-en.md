# #375 "Return Statements"

Shikoku Metan: "Let's organize how return statements work in void functions."
Zundamon: "validate uses conditional return; for early exits, right?"
Shikoku Metan: "Yes, returning without a value is perfectly safe."
Zundamon: "But return "string"; would be an error?"
Shikoku Metan: "Correct—Type 'string' is not assignable to type 'void'."
Zundamon: "So only undefined is acceptable?"
Shikoku Metan: "Exactly; allowed shows both return undefined; and bare return; are valid."
Zundamon: "I'll follow those rules whenever I write void functions!"

---

## 📺 Code for Display

```typescript
/** Example 1: Early returns */
function validate(value: string): void {
  if (!value) return;
  if (value.length < 3) return;
  console.log(`Valid: ${value}`);
}

/** Example 2: Erroneous return */
function invalid(): void {
  return "string";  // Error: cannot return a value
}

/** Example 3: Undefined is allowed */
function allowed(): void {
  return undefined;  // OK
  return;            // Also OK (preferred)
}
```
