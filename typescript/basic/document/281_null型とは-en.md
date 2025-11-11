# #281 "What is the null Type"

Shikoku Metan: "Let's learn about the null type!"
Zundamon: "The null type explicitly represents the absence of a value!"
Shikoku Metan: "That's right. We declare it like let value: null = null;"
Zundamon: "When strictNullChecks is enabled, null handling becomes strict!"
Shikoku Metan: "Exactly. Assigning null to a number type will cause an error."
Zundamon: "We allow it with a union type like number | null!"
Shikoku Metan: "Yes. It's commonly used in function return values and object properties."
Zundamon: "With User | null, we can represent when a user is not found!"

---

## 📺 Code for Display

```typescript
// null type basics
let value: null = null;
let name: string | null = null;
```

```typescript
// When strictNullChecks is enabled
let id: number = null; // Error
let id: number | null = null; // OK
```

```typescript
// Function return values and optional
function findUser(id: number): User | null {
  return users.find(u => u.id === id) ?? null;
}
interface User {
  email: string | null; // Explicit null allowance
}
```
