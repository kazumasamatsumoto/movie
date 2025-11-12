# #453 "Mistake (3) - Returning Values"

Shikoku Metan: "Returning a value from a void function causes errors."
Zundamon: "process returning false was the example."
Shikoku Metan: "If you need a value, change the return type."
Zundamon: "Otherwise just use plain return; for early exit."
Shikoku Metan: "Void functions must never return data."
Zundamon: "I will choose the right return style!"

---

## 📺 Code for Display

```typescript
/** Example 1: Wrong: returning a value */
function process(data: string): void {
  if (!data) {
    return false;
  }
  console.log(data);
}

/** Example 2: Change return type */
function process(data: string): boolean {
  if (!data) {
    return false;
  }
  console.log(data);
  return true;
}

/** Example 3: Void early return */
function process(data: string): void {
  if (!data) return;
  console.log(data);
}
```
