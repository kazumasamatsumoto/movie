# #427 "Promise.all()"

Shikoku Metan: "Understand what Promise.all() actually returns."
Zundamon: "In saveAll, results was void[] and ignored."
Shikoku Metan: "Right, each Promise<void> resolves to undefined."
Zundamon: "Promise.allSettled() lets us inspect successes and failures?"
Shikoku Metan: "Yes, we logged only the rejected entries."
Zundamon: "Promise.race() gave us a timeout pattern!"
Shikoku Metan: "longTask competes with delay to raise a timeout error."
Zundamon: "I'll mix these Promise helpers wisely!"

---

## 📺 Code for Display

```typescript
/** Example 1: Return of Promise.all */
async function saveAll(): Promise<void> {
  const results: void[] = await Promise.all([
    saveData(data1),
    saveData(data2),
    saveData(data3)
  ]);
}

/** Example 2: Promise.allSettled() */
async function processAllSettled(): Promise<void> {
  const results = await Promise.allSettled([task1(), task2(), task3()]);
  results.forEach((result) => {
    if (result.status === "rejected") {
      console.error(result.reason);
    }
  });
}

/** Example 3: Promise.race() */
async function timeout(): Promise<void> {
  await Promise.race([
    longTask(),
    delay(5000).then(() => { throw new Error("Timeout"); })
  ]);
}
```
