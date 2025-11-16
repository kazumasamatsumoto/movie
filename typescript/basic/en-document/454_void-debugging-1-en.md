# #454 "Debugging (1)"

Shikoku Metan: "Even void functions deserve thoughtful debug logs."
Zundamon: "processData logged inputs and early exits."
Shikoku Metan: "update printed info per branch to trace flow."
Zundamon: "Logging doesn't change that we ignore returns?"
Shikoku Metan: "Correct—we only surface side-effect progress."

---

## 📺 Code for Display

```typescript
/** Example 1: Add debug logs */
function processData(data: Data): void {
  console.log('processData called with:', data);
  if (!data.isValid) {
    console.log('Invalid data, returning early');
    return;
  }
  console.log('Processing data...');
  doSomething(data);
  console.log('processData completed');
}

/** Example 2: Branch logging */
function update(user: User): void {
  console.log('update start:', user.id);
  if (user.age < 18) {
    console.log('User is minor');
    return;
  }
  console.log('Updating user');
}

/** Example 3: Trace without returns */
function process(): void {
  console.log('process start');
  step();
  console.log('process end');
}
```
