# #434 "Conditional Types"

Shikoku Metan: "Conditional types can branch on whether a type is void."
Zundamon: "IsVoid<void> was true while IsVoid<number> was false."
Shikoku Metan: "Right, ResultType<T> switches shapes based on the return type."
Zundamon: "AsyncResult<T> chose Promise<void> or Promise<{ data: T }>."
Shikoku Metan: "fetch1 illustrated the void branch."
Zundamon: "So we can automate void-specific behavior."
Shikoku Metan: "Even complex APIs stay type-safe."
Zundamon: "I'll leverage void-aware conditional types!"

---

## 📺 Code for Display

```typescript
/** Example 1: Void detector */

type IsVoid<T> = T extends void ? true : false;
type Test1 = IsVoid<void>;
type Test2 = IsVoid<number>;

/** Example 2: Branch on return type */

type ResultType<T> = T extends void
  ? { success: true }
  : { success: true; data: T };

/** Example 3: Practical example */

type AsyncResult<T> = T extends void
  ? Promise<void>
  : Promise<{ data: T }>;
async function fetch1(): AsyncResult<void> {
  return;
}
```
