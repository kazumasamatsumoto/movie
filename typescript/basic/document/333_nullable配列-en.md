# #333 "Nullable Arrays"

Shikoku Metan: "Let's learn about nullable arrays!"
Zundamon: "It's about processing when array elements are nullable!"
Shikoku Metan: "Yes. With (User | null)[], each element of the array can be User or null."
Zundamon: "How do we exclude null?"
Shikoku Metan: "Exactly. Using filter and the isNotNull type guard function, we can extract only non-null elements."
Zundamon: "We need to be careful when processing with map too!"
Shikoku Metan: "Yes. Like map(u => u?.name ?? "Unknown"), we can process safely using Optional Chaining."
Zundamon: "By properly handling nullable arrays, we can write safe code!"

---

## 📺 Code for Display

```typescript
/** Example 1: Array with nullable elements */
const users: (User | null)[] = [user1, null, user2];
const names = users.filter(u => u !== null);

/** Example 2: Filter with type guard */
function isNotNull<T>(value: T | null): value is T {
  return value !== null;
}
const validUsers = users.filter(isNotNull);

/** Example 3: Map processing */
const userNames = users.map(u => u?.name ?? "Unknown");
```
