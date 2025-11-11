# #270 "Type Guard Summary"

Shikoku Metan: "Let's review and summarize type guards!"
Zundamon: "There were various type guard methods!"
Shikoku Metan: "Yes. typeof is for primitive types, instanceof is for classes."
Zundamon: "in is for object properties, and Array.isArray is for arrays!"
Shikoku Metan: "Exactly. It's important to use each appropriately in the right situations."
Zundamon: "We can also create custom type guards using type predicate functions!"
Shikoku Metan: "Yes. Type predicate functions are useful for complex type checks."
Zundamon: "Now we can write type-safe TypeScript code!"

---

## 📺 Code for Display

```typescript
/** Example 1: Basic type guards */
// typeof - Primitive types
if (typeof value === 'string') { }

// instanceof - Classes
if (value instanceof Date) { }

// in - Object properties
if ('name' in obj) { }

/** Example 2: Arrays and type predicate functions */
// Array.isArray - Arrays
if (Array.isArray(value)) { }

// Type predicate function - Custom type guard
function isUser(obj: unknown): obj is User {
  return typeof obj === 'object' && obj !== null && 'name' in obj;
}
```
