# #411 "Using undefined Returns"

Shikoku Metan: "Functions that return undefined can be consumed as values."
Zundamon: "findUser returns User | undefined, right?"
Shikoku Metan: "Yes, capture the result and inspect it."
Zundamon: "If user !== undefined we can treat it as User?"
Shikoku Metan: "Exactly; the branch safely exposes its properties."
Zundamon: "Optional Chaining plus ?? looks handy too!"
Shikoku Metan: "Expressions like name = findUser(2)?.name ?? 'Unknown' stay compact."
Zundamon: "I'll master working with undefined return values!"

---

## 📺 Code for Display

```typescript
/** Example 1: undefined return value */
function findUser(id: number): User | undefined {
  return users.find(u => u.id === id);
}
const user = findUser(1);

/** Example 2: Check before use */
if (user !== undefined) {
  console.log(user.name);
}

/** Example 3: Optional chaining */
const name = findUser(2)?.name ?? "Unknown";
const email = findUser(3)?.email;
```
