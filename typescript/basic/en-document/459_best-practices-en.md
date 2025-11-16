# #459 "Best Practices"

Shikoku Metan: "Review the core void best practices."
Zundamon: "Declare types explicitly like logMessage or saveData."
Shikoku Metan: "Separate side effects from pure calculations."
Zundamon: "processUser demonstrated chaining small void steps."
Shikoku Metan: "Keep void functions short and intentional."

---

## 📺 Code for Display

```typescript
/** Example 1: Explicit signatures */
function logMessage(msg: string): void {
  console.log(msg);
}
async function saveData(data: Data): Promise<void> {
  await database.save(data);
}

/** Example 2: Separate side effects */
function calculateTotal(items: Item[]): number {
  return items.reduce((sum, item) => sum + item.price, 0);
}
function displayTotal(items: Item[]): void {
  const total = calculateTotal(items);
  console.log(`Total: ${total}`);
}

/** Example 3: Small functions */
function processUser(user: User): void {
  validate(user);
  save(user);
  notify(user);
}
```
