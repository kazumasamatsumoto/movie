# #547 "Mistake (2) - Unreachable Code"

Shikoku Metan: "Never checks fail if you place them too early."
Zundamon: "bad() only handled strings, then tried const check: never = value."
Shikoku Metan: "Numbers remained, so assigning them to never is invalid."
Zundamon: "good() handled string and number before reaching the never check."
Shikoku Metan: "Only when every union member is covered does never make sense."
Zundamon: "Returning check clarifies the code path is unreachable."
Shikoku Metan: "Mind the order of your branches."
Zundamon: "Never should be the final gatekeeper."

---

## 📺 Code for Display

```typescript
/** Example 1: Wrong implementation */
function bad(value: string | number): string {
  if (typeof value === "string") return value;
  const check: never = value;
  return "default";
}
```

```typescript
/** Example 2: Correct implementation */
function good(value: string | number): string {
  if (typeof value === "string") return value;
  if (typeof value === "number") return value.toString();
  const check: never = value;
  return check;
}
```
