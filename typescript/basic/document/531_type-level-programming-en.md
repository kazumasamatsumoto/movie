# #531 "Type-Level Programming"

Shikoku Metan: "Type-level programming shows TypeScript's real power."
Zundamon: "Our If type flipped between True and False branches."
Shikoku Metan: "Reverse<T> recursively expanded arrays to invert them."
Zundamon: "It turned [1,2,3,4] into [4,3,2,1] purely at the type level."
Shikoku Metan: "FilterNever<T> strips never entries to keep arrays clean."
Zundamon: "Only string and number survived, so the type became readable."
Shikoku Metan: "Combine these patterns to tackle advanced algebra."
Zundamon: "Push logic into types and stop bugs before runtime."

---

## 📺 Code for Display

```typescript
/** Example 1: Type-level if */
type If<Cond extends boolean, True, False> =
  Cond extends true ? True : False;

type A = If<true, string, number>;  // string
type B = If<false, string, number>; // number
```

```typescript
/** Example 2: Recursive Reverse */
type Reverse<T extends any[]> =
  T extends [infer First, ...infer Rest]
    ? [...Reverse<Rest>, First]
    : [];

type Result = Reverse<[1, 2, 3, 4]>; // [4, 3, 2, 1]
```

```typescript
/** Example 3: Removing never entries */
type FilterNever<T extends any[]> =
  T extends [infer First, ...infer Rest]
    ? First extends never
      ? FilterNever<Rest>
      : [First, ...FilterNever<Rest>]
    : [];

type Clean = FilterNever<[string, never, number, never]>; // [string, number]
```
