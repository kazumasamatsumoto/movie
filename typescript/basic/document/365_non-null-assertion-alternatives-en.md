# #365 "Alternatives"

Shikoku Metan: "Let's collect safe alternatives to the ! operator."
Zundamon: "The classic type guard is the first option, right?"
Shikoku Metan: "Exactly—wrapping code with if (element !== null) ensures presence."
Zundamon: "Optional Chaining writes it even shorter?"
Shikoku Metan: "Yes, expressions like user?.name ?? 'Unknown' handle nullish values cleanly."
Zundamon: "Can we also build helper type guards for filtering?"
Shikoku Metan: "Define isNotNull to sweep null values out of arrays safely."
Zundamon: "I'll lean on these alternatives before reaching for !."

---

## 📺 Code for Display

```typescript
/** Example 1: Checking with a type guard */
const element = document.getElementById("app");
if (element !== null) {
  element.innerHTML = "Hello";
}

/** Example 2: Optional Chaining */
const user = findUser(id);
const name = user?.name ?? "Unknown";
user?.greet();

/** Example 3: Custom type guard function */
function isNotNull<T>(value: T | null): value is T {
  return value !== null;
}
const validUsers = users.filter(isNotNull);
```
