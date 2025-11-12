# #351 "Nullish Type - T | null | undefined"

Shikoku Metan: "Let's represent missing values with the nullish type (T | null | undefined)!"
Zundamon: "That means the same type accepts both null and undefined, right?"
Shikoku Metan: "Yes, and we can reuse it via a type alias like type Nullish<T> = T | null | undefined."
Zundamon: "Would it help for fields such as a user's email that might be unset?"
Shikoku Metan: "Exactly; it clearly models optional fields like email or age? that may be intentionally blank."
Zundamon: "Is it also handy for the return value of data-fetching functions?"
Shikoku Metan: "Right. Returning User | null | undefined shows not-found cases and invalid IDs."
Zundamon: "I'll model uncertain values safely with the nullish type!"

---

## 📺 Code for Display

```typescript
/** Example 1: Nullish type alias */
type Nullish<T> = T | null | undefined;
let value: string | null | undefined;
value = "hello";
value = null;
value = undefined;

/** Example 2: Using it in a User interface */
interface User {
  name: string;
  email: string | null | undefined;
  age?: number | null;
}

/** Example 3: Function returning a nullish value */
function findUser(id: number): User | null | undefined {
  if (id < 0) return undefined;  // Invalid ID
  const user = database.find(id);
  return user ?? null;           // Fallback when not found
}
```
