# #409 "Compatibility"

Shikoku Metan: "void and undefined are largely assignment-compatible."
Zundamon: "let v: void = undefined; was valid."
Shikoku Metan: "Yes, and the other direction is often fine too."
Zundamon: "Function returns show the difference though?"
Shikoku Metan: "returnsVoid may return undefined, while returnsUndefined is stricter."
Zundamon: "Assigning () => undefined to () => void works?"
Shikoku Metan: "It does, but the opposite may fail."
Zundamon: "I'll follow the compatibility rules carefully!"

---

## 📺 Code for Display

```typescript
/** Example 1: Assignment compatibility */
let v: void = undefined;
let u: undefined = undefined;
let v2: void = u;

/** Example 2: Function returns */
function returnsVoid(): void {
  return undefined;
}
function returnsUndefined(): undefined {
  return undefined;
}

/** Example 3: Function type assignment */
const f1: () => void = (): undefined => undefined;
// const f2: () => undefined = (): void => {};
```
