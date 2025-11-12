# #533 "Type Transformations"

Shikoku Metan: "Never unlocks all kinds of transformations."
Zundamon: "Without<T, U> removes specific members from a union."
Shikoku Metan: "string | number | boolean shrank to just number."
Zundamon: "PickByType<T, ValueType> keeps object properties that match a type."
Shikoku Metan: "name and email survived because they were strings."
Zundamon: "DeepOmit<T, K> recursively stripped every _id."
Shikoku Metan: "Recursive mapping leaves deeply nested data clean."
Zundamon: "Use these transforms to shape API responses."

---

## 📺 Code for Display

```typescript
/** Example 1: Removing union members */
type Without<T, U> = T extends U ? never : T;
type Numbers = Without<string | number | boolean, string | boolean>; // number
```

```typescript
/** Example 2: Picking properties by type */
type PickByType<T, ValueType> = {
  [K in keyof T as T[K] extends ValueType ? K : never]: T[K];
};

type StringProps = PickByType<{
  name: string;
  age: number;
  email: string;
}, string>; // { name: string; email: string }
```

```typescript
/** Example 3: Deep omit */
type DeepOmit<T, K extends string> = {
  [P in keyof T as P extends K ? never : P]:
    T[P] extends object ? DeepOmit<T[P], K> : T[P];
};

type Clean = DeepOmit<{
  _id: string;
  user: { _id: string; name: string };
}, "_id">; // { user: { name: string } }
```
