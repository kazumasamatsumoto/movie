# #340 "Nullable Types Summary"

Shikoku Metan: "Let's summarize nullable types!"
Zundamon: "With Nullable<T> type, we can create types that allow null!"
Shikoku Metan: "Yes. Using T | null, we can explicitly express the absence of a value."
Zundamon: "There are several safe access methods, right?"
Shikoku Metan: "Exactly. We can use Optional Chaining and null checks with the strict equality operator."
Zundamon: "In practical patterns, we combine it with filter!"
Shikoku Metan: "Yes. We can exclude null with the isNotNull function and create safe arrays."
Zundamon: "By mastering nullable types, we can write robust code!"

---

## 📺 Code for Display

```typescript
/** Example 1: Nullable type basics */
type Nullable<T> = T | null;
function findUser(id: number): Nullable<User> {
  return users.find(u => u.id === id) ?? null;
}

/** Example 2: Safe access */
const user = findUser(1);
const name = user?.name ?? "Guest";
if (user !== null) {
  console.log(user.email);
}

/** Example 3: Practical pattern */
const users = getUsers();
const validUsers = users.filter(isNotNull);
const names = validUsers.map(u => u.name);
```
