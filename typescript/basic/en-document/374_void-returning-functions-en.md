# #374 "Functions Returning void"

Shikoku Metan: "Let's review how functions that return void behave."
Zundamon: "log1 shows the basic form with no return at all!"
Shikoku Metan: "Right, though you may still use return; for early exits."
Zundamon: "So log2 returning without a value still counts as void?"
Shikoku Metan: "Exactly; control flow stops but the type stays void."
Zundamon: "Is return undefined; really allowed?"
Shikoku Metan: "Yes, log3 proves the compiler accepts returning undefined."
Zundamon: "Now I understand the return rules for void functions!"

---

## 📺 Code for Display

```typescript
/** Example 1: No return statement */
function log1(msg: string): void {
  console.log(msg);
}

/** Example 2: Return without a value */
function log2(msg: string): void {
  if (!msg) return;
  console.log(msg);
}

/** Example 3: Returning undefined */
function log3(msg: string): void {
  console.log(msg);
  return undefined;
}
```
