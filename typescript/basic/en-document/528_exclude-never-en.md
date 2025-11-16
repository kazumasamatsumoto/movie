# #528 "Exclude<T, never>"

Shikoku Metan: "Did you know Exclude<T, never> changes nothing?"
Zundamon: "Removing never leaves T untouched."
Shikoku Metan: "Passing string or number returns the same union."
Zundamon: "Regular Exclude calls do shrink unions, so the contrast stands out."
Shikoku Metan: "Helpers like RemoveNever<T> get optimized away because never isn't real data."
Zundamon: "string | number | never already equals string | number."
Shikoku Metan: "So meaningless never members don't affect the result."
Zundamon: "Mentally skip them when reading type algebra."

---

## 📺 Code for Display

```typescript
/** Example 1: Behavior of Exclude<T, never> */
type Exclude<T, U> = T extends U ? never : T;
type A = Exclude<string, never>;          // string
type B = Exclude<string | number, never>; // string | number
type C = Exclude<never, never>;           // never
```

```typescript
/** Example 2: Ordinary Exclude usage */
type D = Exclude<string | number, string>; // number
type E = Exclude<"a" | "b" | "c", "a">;   // "b" | "c"
type F = Exclude<string | never, never>;   // string
```

```typescript
/** Example 3: RemoveNever helper */
type RemoveNever<T> = T extends never ? never : T;

type Original = string | number | never; // string | number
type Filtered = RemoveNever<Original>;   // string | number
```
