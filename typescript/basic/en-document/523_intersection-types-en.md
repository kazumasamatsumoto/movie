# #523 "Intersection Types"

Shikoku Metan: "An intersection requires every constraint to hold."
Zundamon: "{ name } & { age } gives a person with both fields."
Shikoku Metan: "string & number collapses to never because they can't coexist."
Zundamon: "A field typed as both string and number is impossible."
Shikoku Metan: "Anything intersected with never produces never."
Zundamon: "object & never or even any & never all disappear."
Shikoku Metan: "Intersecting unions like User & { role: 'admin' } narrows them."
Zundamon: "If we demand role: 'guest' we get never, revealing contradictions."

---

## 📺 Code for Display

```typescript
/** Example 1: Intersection basics */
type WithProfile = { name: string } & { age: number }; // { name: string; age: number }
type Impossible = string & number; // never
type Conflict = { x: string } & { x: number }; // never
```

```typescript
/** Example 2: Intersecting with never */
type Test1 = string & never; // never
type Test2 = number & never; // never
type Test3 = object & never; // never
type Test4 = any & never;    // never
```

```typescript
/** Example 3: Narrowing a union */
type User = { role: "admin" } | { role: "user" };
type Admin = User & { role: "admin" }; // { role: "admin" }
type InvalidRole = User & { role: "guest" }; // never
```
