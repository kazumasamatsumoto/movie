# #282 "Declaring null"

Shikoku Metan: "Let's learn how to declare null!"
Zundamon: "We can declare a pure null type with let value: null = null;!"
Shikoku Metan: "That's right. We can also declare a string type that allows null with string | null."
Zundamon: "We can combine multiple types with null too!"
Shikoku Metan: "Exactly. We write it like string | number | null."
Zundamon: "Arrays can also allow null with string[] | null!"
Shikoku Metan: "Yes. It's important to enable strictNullChecks in tsconfig.json."
Zundamon: "This ensures null safety!"

---

## 📺 Code for Display

```typescript
// Declaring null type
let value: null = null;
let name: string | null = null;
let age: number | null = 25;
```

```typescript
// Multiple types with null
let data: string | number | null = null;
let items: string[] | null = null;
```

```typescript
// tsconfig.json
{
  "compilerOptions": {
    "strictNullChecks": true  // Null safety
  }
}
```
