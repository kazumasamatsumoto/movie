# #422 "Type of await Expressions"

Shikoku Metan: "The type of an await expression depends on the Promise payload."
Zundamon: "Awaiting saveData yields void."
Shikoku Metan: "Right, assigning it to result: void is safe but unused."
Zundamon: "Awaiting Promise.resolve(42) gives a number instead?"
Shikoku Metan: "Exactly—the type matches the resolved value."
Zundamon: "Trying to treat a void await result as string fails."
Shikoku Metan: "Because its type is void, it can't be assigned to another type."
Zundamon: "I'll keep await types in mind to avoid mistakes!"

---

## 📺 Code for Display

```typescript
/** Example 1: Type of await */
async function example(): Promise<void> {
  const result: void = await saveData(data);
}

/** Example 2: Comparing Promise<T> */
async function compare(): Promise<void> {
  const num: number = await Promise.resolve(42);
  const v: void = await Promise.resolve();
}

/** Example 3: Cannot use as value */
async function invalid(): Promise<void> {
  const result = await initialize();
  // const str: string = result;
}
```
