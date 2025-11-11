# #344 "Optional Property Types"

Shikoku Metan「Let's learn about the types of optional properties!」
Zundamon「property?: T is the same as T | undefined!」
Shikoku Metan「Yes. Both express the same type.」
Zundamon「Do we need to check when accessing?」
Shikoku Metan「Exactly. We perform an undefined check before using it safely.」
Zundamon「We can use Optional Chaining too!」
Shikoku Metan「Yes. With the ?. operator, we can safely access even when it's undefined.」
Zundamon「By understanding optional property types, we can access them safely!」

---

## 📺 Code for Display

```typescript
/** Example 1: Equivalence of optional and undefinedable */
interface User1 {
  age?: number;              // number | undefined
}
interface User2 {
  age: number | undefined;   // Same type
}

/** Example 2: Checking when accessing */
const user: User1 = { age: 30 };
if (user.age !== undefined) {
  console.log(user.age + 1);
}

/** Example 3: Safe access with Optional Chaining */
const age = user.age?.toString();
const doubled = user.age ? user.age * 2 : 0;
```
