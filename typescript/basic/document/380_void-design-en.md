# #380 "Design Philosophy"

Shikoku Metan: "Using void lets us separate responsibilities at the design level."
Zundamon: "We can contrast pure functions like add with side-effect ones."
Shikoku Metan: "Exactly—pure functions return numbers, while side-effect functions declare void."
Zundamon: "logResult merely prints a result, so void fits perfectly."
Shikoku Metan: "Yes, the absence of a return value tells readers it's display-only."
Zundamon: "In the DataService interface, getData returns data but saveData/deleteData use void!"
Shikoku Metan: "That separation clarifies that retrieval yields values whereas mutations are side effects."
Zundamon: "I'll treat void as part of my design vocabulary!"

---

## 📺 Code for Display

```typescript
/** Example 1: Pure function */
function add(a: number, b: number): number {
  return a + b;
}

/** Example 2: Side-effect function */
function logResult(result: number): void {
  console.log(`Result: ${result}`);
}

/** Example 3: Clarifying design */
interface DataService {
  getData(): Data;        // Returns data
  saveData(data: Data): void;  // Side effect only
  deleteData(id: number): void;  // Side effect only
}
```
