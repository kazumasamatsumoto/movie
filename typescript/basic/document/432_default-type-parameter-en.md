# #432 "Default Type Parameters"

Shikoku Metan: "Default type parameters keep generics concise."
Zundamon: "Callback<T = void> lets us omit the type argument."
Shikoku Metan: "Exactly; voidCallback works without specifying T."
Zundamon: "But we can still pass number for numberCallback?"
Shikoku Metan: "Yes, override the default whenever needed."
Zundamon: "Handler<TData = void, TResult = void> even showed multiple defaults."
Shikoku Metan: "Defaults make our APIs flexible yet terse."
Zundamon: "I'll leverage them to simplify declarations!"

---

## 📺 Code for Display

```typescript
/** Example 1: Defaulted callback */

type Callback<T = void> = (value: T) => void;
const voidCallback: Callback = (v) => {
  console.log("Callback called");
};

/** Example 2: Explicit type argument */

const numberCallback: Callback<number> = (n) => {
  console.log(n * 2);
};

/** Example 3: Multiple defaults */

type Handler<TData = void, TResult = void> = (data: TData) => TResult;
const logger: Handler = () => {
  console.log("Log");
};
```
