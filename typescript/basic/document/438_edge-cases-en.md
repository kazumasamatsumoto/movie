# #438 "Edge Cases"

Shikoku Metan: "void comes with a few edge cases."
Zundamon: "I was surprised that a Callback = () => void can still return 42."
Shikoku Metan: "Callbacks ignore their return values."
Zundamon: "But function log(): void rejects return 42?"
Shikoku Metan: "Correct—declared void functions are strict."
Zundamon: "forEach callbacks may return x * 2 but the value is dropped."
Shikoku Metan: "Know these quirks to avoid accidental code."
Zundamon: "I'll understand void's edge behavior!"

---

## 📺 Code for Display

```typescript
/** Example 1: Void callback */

type Callback = () => void;
const cb: Callback = () => {
  return 42;
};

/** Example 2: Strict function */

function log(): void {
  // return 42;
}

/** Example 3: forEach example */

[1, 2, 3].forEach((x): void => {
  return x * 2;
});
```
