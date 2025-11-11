# #262 "Null/Undefined Check"

Shikoku Metan「Let's learn about null/undefined checks!」
Zundamon「I want to know how to check strictly!」
Shikoku Metan「Yes. Using === to check individually is the basic approach.」
Zundamon「We check null and undefined separately!」
Shikoku Metan「Exactly. Each has a different meaning, so distinction is important.」
Zundamon「Is there a way to check both together?」
Shikoku Metan「Yes. Using != null excludes both null and undefined.」
Zundamon「Using them appropriately depending on the situation is important!」

---

## 📺 Code for Display

```typescript
/** Example 1: Strict check */
function process(value: string | null | undefined) {
  if (value === null) {
    console.log('null');
  } else if (value === undefined) {
    console.log('undefined');
  } else {
    console.log(value.toUpperCase());
  }
}

/** Example 2: Check both */
function handle(value: string | null | undefined) {
  if (value != null) {
    // Neither null nor undefined
    console.log(value.toUpperCase());
  }
}
```
