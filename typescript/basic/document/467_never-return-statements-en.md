# #467 "Return Statements in never"

Shikoku Metan: "Never functions cannot contain reachable return statements."
Zundamon: "A return after fail() is pointless."
Shikoku Metan: "invalid() reached return; and triggered an error."
Zundamon: "abort() remains valid by throwing at the end."
Shikoku Metan: "If control can return even once, the function is not never."

---

## 📺 Code for Display

```typescript
/** Example 1: Unreachable return */
function fail(message: string): never {
  throw new Error(message);
  // return;
}

/** Example 2: Reachable return error */
function invalid(): never {
  if (Math.random() > 0.5) {
    throw new Error("Error");
  }
  // return;
}

/** Example 3: Correct implementation */
function abort(message: string): never {
  console.error(message);
  throw new Error(message);
}
```
