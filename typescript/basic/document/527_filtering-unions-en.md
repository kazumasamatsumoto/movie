# #527 "Filtering"

Shikoku Metan: "Let's filter unions with conditional types."
Zundamon: "StringsOnly<T> keeps string members and turns the rest into never."
Shikoku Metan: "So 'a' | 'b' | 123 | true | 'c' leaves only the letters."
Zundamon: "FunctionsOnly<T> preserves only function signatures."
Shikoku Metan: "Different parameters still survive as long as they're functions."
Zundamon: "NonNullable removes null/undefined in real-world unions."
Shikoku Metan: "string | null | number | undefined shrank to string | number."
Zundamon: "Chain these filters to sweep away type clutter."

---

## 📺 Code for Display

```typescript
/** Example 1: Keep only strings */
type StringsOnly<T> = T extends string ? T : never;
type Texts = StringsOnly<"a" | "b" | 123 | true | "c">; // "a" | "b" | "c"
```

```typescript
/** Example 2: Keep only functions */
type FunctionsOnly<T> = T extends (...args: any[]) => any ? T : never;

type Functions = FunctionsOnly<
  | string
  | ((x: number) => string)
  | number
  | ((y: string) => number)
>; // ((x: number) => string) | ((y: string) => number)
```

```typescript
/** Example 3: Remove nullable members */
type NonNullable<T> = T extends null | undefined ? never : T;
type Clean = NonNullable<string | null | number | undefined>; // string | number
```
