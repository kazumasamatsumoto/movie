# #256 "What is Type Guard"

Shikoku Metan: "Let's learn about type guards!"
Zundamon: "What do type guards do?"
Shikoku Metan: "They're a mechanism to narrow Union type values to a specific type."
Zundamon: "Like checks such as typeof value === 'string'?"
Shikoku Metan: "Exactly. Inside conditional branches, types are automatically narrowed."
Zundamon: "So toUpperCase() becomes usable only when it's a string!"
Shikoku Metan: "Yes. We can also create custom type guards."
Zundamon: "Use type predicates like obj is User in return values to guarantee types!"

---

## 📺 Code for Display

```typescript
/** Example 1: Union type example */
function processValue(value: string | number) {
  if (typeof value === 'string') {
    // Treated as string type here
    console.log(value.toUpperCase());
  } else {
    // Treated as number type here
    console.log(value.toFixed(2));
  }
}

/** Example 2: Effect of type guard */
type User = { name: string; age: number };
function isUser(obj: unknown): obj is User {
  return typeof obj === 'object' && obj !== null &&
    'name' in obj && 'age' in obj;
}
```
