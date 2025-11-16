# #335 "Nullable Objects"

Shikoku Metan: "Let's learn about nullable objects!"
Zundamon: "It's when a function can return null!"
Shikoku Metan: "Yes. A function that returns User | null returns null when the object is not found."
Zundamon: "How do we access properties?"
Shikoku Metan: "Exactly. We use Optional Chaining like user?.name or user?.age ?? 0."
Zundamon: "We can process safely with type guards!"
Shikoku Metan: "Yes. With if (user !== null), we can treat it as User type inside the block."
Zundamon: "By properly handling nullable objects, we can write safe code!"

---

## 📺 Code for Display

```typescript
/** Example 1: Function returning nullable object */
function findUser(id: number): User | null {
  return users.find(u => u.id === id) ?? null;
}

/** Example 2: Access with Optional Chaining */
const user = findUser(1);
const name = user?.name;
const age = user?.age ?? 0;

/** Example 3: Safe with type guard */
if (user !== null) {
  console.log(user.name); // User type
  console.log(user.age);
}
```
