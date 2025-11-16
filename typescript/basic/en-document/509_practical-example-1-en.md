# #509 "Practical Example (1)"

Shikoku Metan: "Practical example one covers a numeric reducer."
Zundamon: "The Action union had increment, decrement, and reset."
Shikoku Metan: "The reducer used if chains and ended with const check: never = action;."
Zundamon: "Any new action instantly surfaces as a compile error."
Shikoku Metan: "When we add multiply, the reducer complains because it's unhandled."
Zundamon: "Payload-carrying types still cooperate with never checks."
Shikoku Metan: "That setup lets us grow the action list safely."
Zundamon: "Never keeps unions sturdy even in production reducers."

---

## 📺 Code for Display

```typescript
/** Example 1: Counter actions */
type Action =
  | { type: "increment"; payload: number }
  | { type: "decrement"; payload: number }
  | { type: "reset" };

/** Example 2: Reducer with never check */
function reducer(state: number, action: Action): number {
  if (action.type === "increment") return state + action.payload;
  if (action.type === "decrement") return state - action.payload;
  if (action.type === "reset") return 0;
  const check: never = action;
  return state;
}

/** Example 3: Detecting new actions */
type ExtendedAction =
  | { type: "increment"; payload: number }
  | { type: "decrement"; payload: number }
  | { type: "reset" }
  | { type: "multiply"; payload: number };

// The reducer must add a branch for multiply or the compiler errors
```
