# #451 "Mistake (1) - Using void Returns"

Shikoku Metan: "Trying to consume void returns is a common mistake."
Zundamon: "I once assigned log() to a string and got an error!"
Shikoku Metan: "Expressions like update() + 1 are invalid too."
Zundamon: "So the fix is to call the function for its side effect only?"
Shikoku Metan: "Exactly—just invoke process(); and ignore the result."
Zundamon: "Whenever I see void, I will not touch the return value!"

---

## 📺 Code for Display

```typescript
/** Example 1: Mistake: using the return */
function log(msg: string): void {
  console.log(msg);
}
const result: string = log("Hello");

/** Example 2: Mistake: arithmetic */
function update(): void {
  count++;
}
const value = update() + 1;

/** Example 3: Correct usage */
function process(): void {
  doSomething();
}
process();
console.log("Done");
```
