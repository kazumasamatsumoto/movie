# #475 "Basics Summary"

Shikoku Metan: "Let's recap the essentials of never."
Zundamon: "Only throwers or infinite loops qualify."
Shikoku Metan: "Use it for functions like fail() that never return."
Zundamon: "And remember exhaustiveCheck."
Shikoku Metan: "Master the basics to handle advanced cases."
Zundamon: "I won't fear never anymore!"

---

## 📺 Code for Display

```typescript
/** Example 1: Throw example */
function throwError(message: string): never {
  throw new Error(message);
}

/** Example 2: Infinite loop */
function serve(): never {
  while (true) handleRequest();
}

/** Example 3: Exhaustive helper */
function exhaustiveCheck(value: never): never {
  throw new Error(`Unhandled: ${value}`);
}
```
