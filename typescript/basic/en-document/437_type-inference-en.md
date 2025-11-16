# #437 "Type Inference"

Shikoku Metan: "Type inference often yields void."
Zundamon: "execute(() => console.log()) returned void automatically."
Shikoku Metan: "Async functions without returns infer Promise<void>."
Zundamon: "When needed we can specify execute<void>(() => ...), right?"
Shikoku Metan: "Exactly."
Zundamon: "I'll balance inference and explicit types!"

---

## 📺 Code for Display

```typescript
/** Example 1: Void inference */

function execute<T>(fn: () => T): T {
  return fn();
}
const result = execute(() => {
  console.log("Done");
});

/** Example 2: Promise inference */

async function process() {
  await doSomething();
}

/** Example 3: Explicit annotation */

const result2 = execute<void>(() => {
  console.log("Done");
});
```
