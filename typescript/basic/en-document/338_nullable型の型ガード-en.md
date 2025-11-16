# #338 "Type Guards for Nullable Types"

Shikoku Metan: "Let's learn about type guards for nullable types!"
Zundamon: "We can check for null with type guard functions!"
Shikoku Metan: "Yes. With the isNotNull function, we can guarantee at the type level that a value is not null."
Zundamon: "The syntax 'value is T' is important, right?"
Shikoku Metan: "Exactly. This allows TypeScript to automatically narrow down the type."
Zundamon: "We can combine it with array filter!"
Shikoku Metan: "Yes. We can safely create an array excluding null from an array containing null."
Zundamon: "With type guards, we can write type-safe code!"

---

## 📺 Code for Display

```typescript
/** Example 1: Type guard function */
function isNotNull<T>(value: T | null): value is T {
  return value !== null;
}

/** Example 2: Usage example */
const user: User | null = getUser();
if (isNotNull(user)) {
  user.name; // Can be treated as User type
}

/** Example 3: Combining with array filter */
const users: (User | null)[] = [user1, null, user2];
const validUsers: User[] = users.filter(isNotNull);
```
