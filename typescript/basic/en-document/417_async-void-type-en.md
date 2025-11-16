# #417 "void Types in async Functions"

Shikoku Metan: "Async functions always return Promises."
Zundamon: "process(): Promise<void> was the correct signature."
Shikoku Metan: "Yes, async function process(): void would fail."
Zundamon: "Is it fine to rely on inference with async function load()?"
Shikoku Metan: "If it returns nothing, TypeScript infers Promise<void>."
Zundamon: "So we think in void terms but wrap them in Promise."
Shikoku Metan: "Exactly—remember Promise<void> for async side effects."
Zundamon: "I'll declare async void-style functions properly!"

---

## 📺 Code for Display

```typescript
/** Example 1: Correct signature */
async function process(): Promise<void> {
  await doSomething();
  console.log("Done");
}

/** Example 2: Invalid signature */
// async function process(): void {
//   await doSomething();
// }

/** Example 3: Type inference */
async function load() {
  await fetch("/api/data");
}
```
