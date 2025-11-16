# #306 "Difference Between undefined and void"

Shikoku Metan: "Let's learn about the difference between undefined and void!"
Zundamon: "So the void type indicates that return values are not used!"
Shikoku Metan: "That's right. The undefined type is used when explicitly returning undefined."
Zundamon: "Even functions that return void actually return undefined, right?"
Shikoku Metan: "Exactly. void shows the intention at the type level that the return value won't be used."
Zundamon: "The undefined type can be used in union types to express cases where values don't exist!"
Shikoku Metan: "By distinguishing them in function return types, the code's intention becomes clear."
Zundamon: "void is for functions with side effects, while undefined type is for functions that might return values!"

---

## 📺 Code for Display

```typescript
/** Example 1: void type - return value not used */
function log(msg: string): void {
  console.log(msg);
}
log("Hello"); // return value cannot be used

/** Example 2: undefined type - explicitly undefined */
function find(): User | undefined {
  return undefined;
}
const user = find(); // undefined

/** Example 3: void returns undefined */
function noReturn(): void { }
const result = noReturn(); // undefined (type is void)
```
