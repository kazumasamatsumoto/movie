# #280 "Master Check"

Shikoku Metan: "Let's do a master check of boolean types!"
Zundamon: "We check value === null with the strict equality operator ===!"
Shikoku Metan: "That's right. We use the isUser function with type guards to safely narrow down types."
Zundamon: "Falsy values are the six: false, 0, empty string, null, undefined, and NaN, right?"
Shikoku Metan: "Exactly. Understanding and handling these correctly is important."
Zundamon: "In Angular/Nest.js, we use the @IsBoolean() decorator!"
Shikoku Metan: "Yes. Combining strictNullChecks and ESLint is the best practice."
Zundamon: "Now we've completely mastered boolean types!"

---

## 📺 Code for Display

```typescript
// ✅ Strict equality operator
if (value === null) { }

// ✅ Type guard
function isUser(obj: unknown): obj is User {
  return typeof obj === 'object' && obj !== null && 'name' in obj;
}

// ✅ Understanding falsy values
// false, 0, '', null, undefined, NaN
```

```typescript
// ✅ Practice in Angular/Nest.js
@IsBoolean() isActive: boolean;

// ✅ Best practices
// strictNullChecks + ESLint
```
