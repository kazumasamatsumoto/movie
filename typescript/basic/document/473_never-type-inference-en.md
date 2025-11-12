# #473 "Type Inference"

Shikoku Metan: "TypeScript infers never when a function only throws."
Zundamon: "fail(message) was inferred automatically."
Shikoku Metan: "Use explicit annotations like abort(message): never when clarity helps."
Zundamon: "In exhaustive conditionals, the remaining code becomes never?"
Shikoku Metan: "Exactly, it's marked unreachable."
Zundamon: "I'll balance inference and annotations!"

---

## 📺 Code for Display

```typescript
/** Example 1: Inferred never */
function fail(message: string) {
  throw new Error(message);
}

/** Example 2: Explicit annotation */
function abort(message: string): never {
  throw new Error(message);
}

/** Example 3: Conditional inference */
function process(value: string | number) {
  if (typeof value === "string") {
    return value.length;
  } else {
    return value * 2;
  }
  // unreachable, inferred never
}
```
