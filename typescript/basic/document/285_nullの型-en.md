# #285 "The null Type"

Shikoku Metan: "Let's learn about the null type in detail!"
Zundamon: "We can define a pure null type with let value: null = null;!"
Shikoku Metan: "That's right. We can also create a type alias like type NullType = null."
Zundamon: "It's interesting that typeof null is "object"!"
Shikoku Metan: "That's an old JavaScript specification. We need to be careful."
Zundamon: "Setting strictNullChecks to true improves type safety!"
Shikoku Metan: "Yes. Assigning null to a string type causes an error."
Zundamon: "We can exclude null with NonNullable<T>!"

---

## 📺 Code for Display

```typescript
// null type and typeof
let value: null = null;
type NullType = null;
typeof null; // "object" (JavaScript specification)
```

```typescript
// strictNullChecks: true
let str: string = null;  // Error
let str: string | null = null;  // OK
```

```typescript
// Exclude with NonNullable<T>
type Result = string | number | null;
type NonNull = NonNullable<Result>;
// → string | number
```
