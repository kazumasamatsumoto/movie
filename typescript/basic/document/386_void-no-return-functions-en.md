# #386 "Functions Without Returns"

Shikoku Metan: "Let's outline functions that lack return values."
Zundamon: "greet has no return statement, so it's treated as void."
Shikoku Metan: "Yes, assigning its result gives you undefined at runtime."
Zundamon: "Should updateCounter, which only mutates state, also be void?"
Shikoku Metan: "Exactly—its sole job is side effects."
Zundamon: "Knowing the runtime result is undefined makes things clear!"
Shikoku Metan: "Remember: void in the type system corresponds to undefined at runtime."
Zundamon: "I'll write void functions with that behavior in mind!"

---

## 📺 Code for Display

```typescript
/** Example 1: No-return function */
function greet(name: string): void {
  console.log(`Hello, ${name}`);
}

/** Example 2: Runtime undefined */
const result = greet("Alice");
console.log(result);  // undefined

/** Example 3: Function for side effects */
function updateCounter(): void {
  counter++;
  render();
}
```
