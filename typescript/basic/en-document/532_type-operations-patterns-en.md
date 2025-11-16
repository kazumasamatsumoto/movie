# #532 "Type Operation Patterns"

Shikoku Metan: "Let's catalog common type-operation patterns."
Zundamon: "Filter<T, Condition> keeps only members that satisfy the condition."
Shikoku Metan: "It pulled just the strings out of 'a' | 'b' | 1 | 2."
Zundamon: "MapToArray<T> turns every property into an array."
Shikoku Metan: "name became string[] and age became number[]."
Zundamon: "Match<T> branched into String/Number/Boolean/Unknown labels."
Shikoku Metan: "That feels like pattern matching at the type level."
Zundamon: "Mix these patterns to boost your expressiveness."

---

## 📺 Code for Display

```typescript
/** Example 1: Filtering pattern */
type Filter<T, Condition> =
  T extends Condition ? T : never;

type Strings = Filter<"a" | "b" | 1 | 2, string>; // "a" | "b"
```

```typescript
/** Example 2: Mapping properties to arrays */
type MapToArray<T> = {
  [K in keyof T]: T[K][];
};

type Arrays = MapToArray<{ name: string; age: number }>; // { name: string[]; age: number[] }
```

```typescript
/** Example 3: Type-based matching */
type Match<T> =
  T extends string ? "String"
  : T extends number ? "Number"
  : T extends boolean ? "Boolean"
  : "Unknown";

type M1 = Match<"hello">; // "String"
type M2 = Match<42>;      // "Number"
type M3 = Match<object>;  // "Unknown"
```
