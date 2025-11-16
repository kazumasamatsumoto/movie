# #405 "Assigning to undefined-typed Variables"

Shikoku Metan: "Variables typed as undefined accept only undefined."
Zundamon: "Right, we assigned undefined to value: undefined in the sample."
Shikoku Metan: "Null or numbers trigger errors."
Zundamon: "A union like string | undefined lets us toggle between data and undefined?"
Shikoku Metan: "Exactly, that's what the data variable shows."
Zundamon: "Functions such as getValue(): string | undefined are common too."
Shikoku Metan: "They highlight when a value might be missing."
Zundamon: "I'll master undefined-typed variables!"

---

## 📺 Code for Display

```typescript
/** Example 1: undefined variable */
let value: undefined;
value = undefined;  // OK

/** Example 2: Union type */
let data: string | undefined;
data = "hello";
data = undefined;

/** Example 3: Function return */
function getValue(): string | undefined {
  if (Math.random() > 0.5) {
    return "value";
  }
  return undefined;
}
```
