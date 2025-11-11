# #279 "Best Practices"

Shikoku Metan: "Let's learn about best practices for boolean types!"
Zundamon: "First, we must always use the strict equality operator ===!"
Shikoku Metan: "That's right. We check types clearly, like value === null."
Zundamon: "Using type guards can further enhance type safety, right?"
Shikoku Metan: "Exactly. We can narrow down types with typeof val === 'string'."
Zundamon: "Explicit type annotations like const isActive: boolean are important too!"
Shikoku Metan: "Yes. strictNullChecks and ESLint configuration are also essential."
Zundamon: "We prohibit == with 'eqeqeq': ['error', 'always']!"

---

## 📺 Code for Display

```typescript
// ✅ Using strict equality operator
if (value === null) { }

// ✅ Utilizing type guards
function isString(val: unknown): val is string {
  return typeof val === 'string';
}

// ✅ Explicit type annotations
const isActive: boolean = true;
```

```typescript
// ✅ Enabling strictNullChecks
// tsconfig.json
// "strictNullChecks": true

// ✅ ESLint configuration
// "eqeqeq": ["error", "always"]
```
