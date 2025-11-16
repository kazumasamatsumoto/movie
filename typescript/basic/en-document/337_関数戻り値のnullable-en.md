# #337 "Nullable Function Return Values"

Shikoku Metan: "Let's learn about nullable function return values!"
Zundamon: "We can make function return values nullable types!"
Shikoku Metan: "Yes. By returning User | null, we can express not-found cases with null."
Zundamon: "Do we need to check for null on the caller side?"
Shikoku Metan: "Exactly. With if (user !== null), we write the processing for non-null cases."
Zundamon: "We can use Nullish Coalescing too!"
Shikoku Metan: "Yes. With the ?? operator, we can write concise default handling for null cases."
Zundamon: "With nullable return values, we can design safe functions!"

---

## 📺 Code for Display

```typescript
/** Example 1: nullable return value */
function findUser(id: number): User | null {
  const user = users.find(u => u.id === id);
  return user ?? null;
}

/** Example 2: Caller-side processing */
const user = findUser(1);
if (user !== null) {
  console.log(user.name);
}

/** Example 3: Concise with Nullish Coalescing */
const user = findUser(1) ?? createGuestUser();
const name = findUser(1)?.name ?? "Unknown";
```
