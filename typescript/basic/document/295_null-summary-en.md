# #295 "Null Type Summary"

Shikoku Metan「Let's learn the null type summary!」
Zundamon「We're organizing what we've learned so far!」
Shikoku Metan「Yes. First, explicitly handle null with Union types.」
Zundamon「Check with !== null before using it!」
Shikoku Metan「Exactly. You can also set default values with Nullish Coalescing ??.」
Zundamon「It's convenient when combined with optional chaining ?.!」
Shikoku Metan「Yes. It's also commonly used in practical Repository patterns.」
Zundamon「Handle null type-safely to prevent bugs!」

---

## 📺 Code for Display

```typescript
/** Example 1: Null type basics */
let value: string | null = null;
if (value !== null) {
  value.toUpperCase(); // string type
}

/** Example 2: Nullish Coalescing */
const name = userName ?? "Guest";
const config = settings?.timeout ?? 5000;

/** Example 3: Practical pattern */
function findUser(id: number): User | null {
  return users.find(u => u.id === id) ?? null;
}
```
