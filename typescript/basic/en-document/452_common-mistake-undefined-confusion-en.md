# #452 "Mistake (2) - Confusing undefined"

Shikoku Metan: "Another mistake is confusing void with undefined."
Zundamon: "getValue(): void returning undefined felt strange."
Shikoku Metan: "If you need to return the value undefined, type it as Item | undefined."
Zundamon: "So void equals side effects, undefined equals optional data."
Shikoku Metan: "Distinguish them to keep callers safe."
Zundamon: "I will never mix them up again!"

---

## 📺 Code for Display

```typescript
/** Example 1: Wrong: mixing void/undefined */
function getValue(): void {
  return undefined;
}
const value = getValue();

/** Example 2: Correct: return undefined */
function findItem(id: number): Item | undefined {
  return items.find(item => item.id === id);
}
const item = findItem(1);
if (item !== undefined) {
  console.log(item.name);
}

/** Example 3: Correct: void for side effect */
function logMessage(msg: string): void {
  console.log(msg);
}
logMessage("Hello");
```
