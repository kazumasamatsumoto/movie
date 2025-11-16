# #376 "void vs undefined"

Shikoku Metan: "Let's differentiate void from undefined."
Zundamon: "void means "ignore the return", while undefined is an actual value, right?"
Shikoku Metan: "Exactly; result1 from logMessage is void to show there's nothing to use."
Zundamon: "findItem returns Item | undefined, so callers must check the result?"
Shikoku Metan: "Yes, that function's return value carries data or undefined."
Zundamon: "So the Logger vs Finder types illustrate the separation of roles."
Shikoku Metan: "Use void for side effects and unions with undefined for optional data."
Zundamon: "I'll keep the distinction clear in my head!"

---

## 📺 Code for Display

```typescript
/** Example 1: void: ignore the result */
function logMessage(msg: string): void {
  console.log(msg);
}
const result1 = logMessage("Hello");  // void type

/** Example 2: undefined: actual value */
function findItem(id: number): Item | undefined {
  return items.find(item => item.id === id);
}
const result2 = findItem(1);  // Item | undefined

/** Example 3: Choosing between them */
type Logger = (msg: string) => void;      // Side effects
type Finder = (id: number) => Item | undefined;  // Lookup
```
