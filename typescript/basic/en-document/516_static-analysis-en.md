# #516 "Static Analysis"

Shikoku Metan: "Never pairs nicely with static analysis."
Zundamon: "validate() only allowed GET/POST and stopped others via const check: never."
Shikoku Metan: "Uncovered HTTP methods stand out during reviews."
Zundamon: "process() checked for null, then analysis knew toUpperCase() was safe."
Shikoku Metan: "greet() switched output once age was present."
Zundamon: "Trustworthy control-flow analysis needs precise narrowing."
Shikoku Metan: "Helpers that return never signal tools to flag gaps."
Zundamon: "Let types and analysis double-team your safety net."

---

## 📺 Code for Display

```typescript
/** Example 1: HTTP method validation */
type HttpMethod = "GET" | "POST" | "PUT" | "DELETE";

function validate(method: HttpMethod): boolean {
  if (method === "GET") return true;
  if (method === "POST") return true;
  const check: never = method;
  return false;
}

/** Example 2: Control-flow analysis */
function process(value: string | null): string {
  if (value === null) {
    return "null";
  }
  return value.toUpperCase();
}

/** Example 3: Data-flow analysis */
type User = { name: string; age?: number };

function greet(user: User): string {
  if (user.age !== undefined) {
    return `${user.name} (${user.age})`;
  }
  return user.name;
}
```
