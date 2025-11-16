# #410 "Using void Returns"

Shikoku Metan: "Never consume a void return value."
Zundamon: "Assigning log('Hello') to string causes an error."
Shikoku Metan: "Yes, but storing it in voidValue: void is fine."
Zundamon: "The runtime still yields undefined though—does type checking stop misuse?"
Shikoku Metan: "process() returns undefined, yet its type is void so it can't be assigned elsewhere."
Zundamon: "I'll respect void and ignore the return!"
Shikoku Metan: "Exactly—focus on the side effects."

---

## 📺 Code for Display

```typescript
/** Example 1: void return cannot be used */
function log(msg: string): void {
  console.log(msg);
}
const result: string = log("Hello");

/** Example 2: Assignable to void variable */
const voidValue: void = log("Test");

/** Example 3: Runtime undefined */
function process(): void {
  return;
}
const value = process();
console.log(value);
```
