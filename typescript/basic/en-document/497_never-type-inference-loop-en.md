# #497 "Type Inference"

Shikoku Metan: "TypeScript infers never or void based on loop exit."
Zundamon: "loop1() never breaks, so it's never."
Shikoku Metan: "loop2() can break and becomes void."
Zundamon: "loop3() returns when forever is false, so it's void as well."
Shikoku Metan: "Add annotations when inference doesn't match your intent."

---

## 📺 Code for Display

```typescript
/** Example 1: Inferred never */
function loop1() {
  while (true) {
    doWork();
  }
}

/** Example 2: Inferred void */
function loop2() {
  while (true) {
    doWork();
    if (shouldStop()) {
      break;
    }
  }
}

/** Example 3: Conditional exit */
function loop3(forever: boolean) {
  while (true) {
    process();
    if (!forever) return;
  }
}
```
