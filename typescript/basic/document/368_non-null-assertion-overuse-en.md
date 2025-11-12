# #368 "Mistake (3) - Overusing !"

Shikoku Metan: "Spamming ! makes the code's intent disappear."
Zundamon: "Chains like response.data!.users!.find(...)! look terrifying."
Shikoku Metan: "Exactly—if any link is null you'll blow up instantly."
Zundamon: "Adding type guards would help readability and safety?"
Shikoku Metan: "Yes, check that users exists and verify profile?.name before using it."
Zundamon: "Can lint rules forbid the operator as well?"
Shikoku Metan: "Set @typescript-eslint/no-non-null-assertion to error to discourage overuse."
Zundamon: "I'll build an environment where ! appears only when justified!"

---

## 📺 Code for Display

```typescript
/** Example 1: Example of overuse */
const data = response.data!.users!.find(u => u.id === id)!;
const name = data.profile!.name!.toUpperCase();

/** Example 2: Proper type guards */
if (response.data?.users) {
  const user = response.data.users.find(u => u.id === id);
  if (user?.profile?.name) {
    const name = user.profile.name.toUpperCase();
  }
}

/** Example 3: Restricting it with ESLint */
// .eslintrc.json
{
  "rules": {
    "@typescript-eslint/no-non-null-assertion": "error"
  }
}
```
