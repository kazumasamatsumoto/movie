# #358 "Optional Chaining - ?."

Shikoku Metan: "Let's revisit the Optional Chaining operator ?."
Zundamon: "user?.name won't crash even if user is null, right?"
Shikoku Metan: "Correct, property access becomes safe and short."
Zundamon: "Can we use it for method calls?"
Shikoku Metan: "obj?.method?.() calls only when both the object and method exist."
Zundamon: "Does it work for arrays and deeply nested fields?"
Shikoku Metan: "array?.[0] and user?.contacts?.[0]?.phone handle those cases nicely."
Zundamon: "Optional Chaining frees us from endless undefined checks!"

---

## 📺 Code for Display

```typescript
/** Example 1: Property access */
const user: User | null | undefined = getUser();
const name = user?.name;
const email = user?.email;

/** Example 2: Method calls */
const result = obj?.method?.();
const length = str?.toUpperCase()?.length;

/** Example 3: Array access and nesting */
const firstItem = array?.[0];
const city = user?.address?.city;
const phone = user?.contacts?.[0]?.phone;
```
