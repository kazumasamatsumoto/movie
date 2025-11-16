# #522 "string | never = string"

Shikoku Metan: "The identity string | never = string is a classic."
Zundamon: "Numbers or custom MyType behave the same way."
Shikoku Metan: "Exclude<T, U> works because disallowed members become never."
Zundamon: "That's why Result1 leaves only 'b' | 'c'."
Shikoku Metan: "ReturnTypeFilter discards functions that return void."
Zundamon: "Only string-returning functions remain, which cleans up APIs."
Shikoku Metan: "Blend never into unions to trim unwanted pieces."
Zundamon: "It's like a type-level vacuum cleaner."

---

## 📺 Code for Display

```typescript
/** Example 1: string | never identity */
type Test1 = string | never;            // string
type Test2 = number | never;            // number
type Test3 = MyType | never;            // MyType
type Test4 = (string | number) | never; // string | number
```

```typescript
/** Example 2: Exclude mechanics */
type Exclude<T, U> = T extends U ? never : T;

type Result1 = Exclude<"a" | "b" | "c", "a">; // "b" | "c"
type Result2 = Exclude<string | number, string>; // number
```

```typescript
/** Example 3: Filtering return types */
type ReturnTypeFilter<T> =
  T extends (...args: any[]) => infer R
    ? R extends void ? never : R
    : never;

type OnlyString = ReturnTypeFilter<() => string>; // string
type RemovedVoid = ReturnTypeFilter<() => void>;  // never
```
