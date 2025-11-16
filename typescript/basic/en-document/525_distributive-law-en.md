# #525 "Distributive Law"

Shikoku Metan: "Conditional types distribute over unions."
Zundamon: "That's why ToArray<string | number> becomes string[] | number[]."
Shikoku Metan: "Exclude performs the same member-by-member filtering."
Zundamon: "Only 'b' | 'c' survive after removing 'a'."
Shikoku Metan: "Wrap T in a tuple, like NoDistribute, to stop distribution."
Zundamon: "Then you keep (string | number)[] as a single chunk."
Shikoku Metan: "Controlling distribution leads to precise type algebra."
Zundamon: "Use it wisely once you grasp how never behaves."

---

## 📺 Code for Display

```typescript
/** Example 1: Distributing ToArray */
type ToArray<T> = T extends any ? T[] : never;
type Result = ToArray<string | number>; // string[] | number[]
```

```typescript
/** Example 2: Exclude distribution */
type Exclude<T, U> = T extends U ? never : T;
type Filtered = Exclude<"a" | "b" | "c", "a">; // "b" | "c"
```

```typescript
/** Example 3: Preventing distribution */
type NoDistribute<T> = [T] extends [any] ? T[] : never;

type Result1 = NoDistribute<string | number>; // (string | number)[]
type Result2 = ToArray<string | number>; // string[] | number[]
```
