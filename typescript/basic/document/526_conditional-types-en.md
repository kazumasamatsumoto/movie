# #526 "Conditional Types"

Shikoku Metan: "Conditional types behave like type-level if statements."
Zundamon: "IsString<T> returns true for strings and false otherwise."
Shikoku Metan: "Filter<T> lets only string members through and turns the rest into never."
Zundamon: "So string | number | boolean shrank to string."
Shikoku Metan: "FunctionKeys<T> pulled out only the method names."
Zundamon: "We ended up with just getName()."
Shikoku Metan: "Conditional types let us sculpt union members freely."
Zundamon: "Pair them with never to smartly select types."

---

## 📺 Code for Display

```typescript
/** Example 1: IsString utility */
type IsString<T> = T extends string ? true : false;
type A = IsString<string>;  // true
type B = IsString<number>;  // false
type C = IsString<"hello">; // true
```

```typescript
/** Example 2: Filter that keeps strings only */
type Filter<T> = T extends string ? T : never;
type Result = Filter<string | number | boolean>; // string
```

```typescript
/** Example 3: Extracting function keys */
type FunctionKeys<T> = {
  [K in keyof T]: T[K] extends Function ? K : never
}[keyof T];

type Methods = FunctionKeys<{
  name: string;
  getName(): string;
  age: number;
}>; // "getName"
```
