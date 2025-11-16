# #465 "Declaring never"

Shikoku Metan: "We declare never mostly on function returns."
Zundamon: "throwError(message): never is the template."
Shikoku Metan: "Variables typed as never rarely appear and reject assignments."
Zundamon: "Do throw-only functions infer never automatically?"
Shikoku Metan: "Yes, fail() becomes never because it never returns."
Zundamon: "I'll balance explicit declarations with inference!"

---

## 📺 Code for Display

```typescript
/** Example 1: Function declaration */
function throwError(message: string): never {
  throw new Error(message);
}

/** Example 2: Variable declaration */
let neverValue: never;
// neverValue = 1;

/** Example 3: Type inference */
function fail(msg: string) {
  throw new Error(msg);
}
```
