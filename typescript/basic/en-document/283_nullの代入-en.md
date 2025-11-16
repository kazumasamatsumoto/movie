# #283 "Assigning null"

Shikoku Metan: "Let's learn about assigning null!"
Zundamon: "A variable of type string | null can be assigned both null and strings!"
Shikoku Metan: "That's right. Both name = "Alice" and name = null; are fine."
Zundamon: "When strictNullChecks is enabled, restrictions become stricter!"
Shikoku Metan: "Exactly. Assigning null to a number type causes an error."
Zundamon: "We need to explicitly declare it as number | null!"
Shikoku Metan: "Yes. It's also commonly used in function parameters and object properties."
Zundamon: "We can clear user information with User | null!"

---

## 📺 Code for Display

```typescript
// Assigning null
let name: string | null = null;
name = "Alice";  // OK
name = null;     // OK
```

```typescript
// When strictNullChecks is enabled
let id: number = null;  // Error
let id: number | null = null;  // OK
```

```typescript
// Function parameters and objects
function setUser(user: User | null): void {
  currentUser = user;
}
interface Config {
  cache: CacheService | null;
}
```
