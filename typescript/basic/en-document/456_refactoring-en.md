# #456 "Refactoring"

Shikoku Metan: "When refactoring void functions, split responsibilities."
Zundamon: "We separated calculate and display."
Shikoku Metan: "Chaining small void helpers improves testability."
Zundamon: "Also confirm we never rely on return values internally."
Shikoku Metan: "Well-named void helpers boost readability."

---

## 📺 Code for Display

```typescript
/** Example 1: Split responsibilities */
function calculateTotal(items: Item[]): number {
  return items.reduce((sum, item) => sum + item.price, 0);
}
function displayTotal(items: Item[]): void {
  const total = calculateTotal(items);
  console.log(`Total: ${total}`);
}

/** Example 2: Smaller void helpers */
function validate(user: User): void {
  // ...
}
function save(user: User): void {
  // ...
}
function processUser(user: User): void {
  validate(user);
  save(user);
}

/** Example 3: Remove return dependency */
function process(): void {
  step1();
  step2();
}
```
