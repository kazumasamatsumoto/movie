# #325 "strictNullChecks Summary"

Shikoku Metan: "Let's summarize strictNullChecks!"
Zundamon: "We enable everything with strict mode!"
Shikoku Metan: "That's right. Setting strict to true also enables strictNullChecks."
Zundamon: "Writing type-safe code is important, right?"
Shikoku Metan: "Exactly. Process safely with null checks and default values."
Zundamon: "We've learned practical patterns too!"
Shikoku Metan: "Yes. Combine optional chaining and Nullish Coalescing."
Zundamon: "We write null-safe code with strictNullChecks!"

---

## 📺 Code for Display

```typescript
/** Example 1: Essential configuration */
{
  "compilerOptions": {
    "strict": true  // strictNullChecksも有効
  }
}

/** Example 2: Type-safe code */
function process(value: string | null): string {
  if (value === null) return "default";
  return value.toUpperCase();
}

/** Example 3: Practical patterns */
const user = getUser();
const name = user?.name ?? "Guest";
if (user !== null) {
  console.log(user.email);
}
```
