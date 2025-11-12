# #535 "Type Operation Recap"

Shikoku Metan: "Time to recap our type operations."
Zundamon: "Laws 1-4 cover union/intersection plus Exclude/Extract basics."
Shikoku Metan: "Remember string | never = string and string & never = never."
Zundamon: "Helpers like NonNullable, FunctionKeys, and PickByType shine in practice."
Shikoku Metan: "DeepPartial softens nested structures."
Zundamon: "Result<T, E> style discriminated unions power error handling."
Shikoku Metan: "Combine these pieces for a robust type system."
Zundamon: "Understand never and every operation becomes an ally."

---

## 📺 Code for Display

```typescript
/** Example 1: Core laws */
type Law1 = string | never;    // string
type Law2 = string & never;    // never
type Law3<T> = Exclude<T, never>; // T
type Law4<T> = Extract<never, T>; // never
```

```typescript
/** Example 2: Practical helpers */
type NonNullable<T> = T extends null | undefined ? never : T;
type FunctionKeys<T> = {
  [K in keyof T]: T[K] extends Function ? K : never
}[keyof T];
type PickByType<T, U> = {
  [K in keyof T as T[K] extends U ? K : never]: T[K]
};
```

```typescript
/** Example 3: Composite operations */
type DeepPartial<T> = {
  [K in keyof T]?: T[K] extends object ? DeepPartial<T[K]> : T[K];
};

type Result<T, E> =
  | { ok: true; value: T }
  | { ok: false; error: E };
```
