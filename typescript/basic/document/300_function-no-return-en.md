# #300 "Functions with No Return Value"

Shikoku Metan「Let's learn about functions with no return value!」
Zundamon「What's the difference between void and undefined types?」
Shikoku Metan「Yes. void type doesn't use return values, undefined type explicitly returns undefined.」
Zundamon「void functions implicitly return undefined!」
Shikoku Metan「Exactly. When there's no return statement, undefined is automatically returned.」
Zundamon「Do find functions return User | undefined?」
Shikoku Metan「Yes. A design that returns undefined when not found is commonly used.」
Zundamon「It's important to make intent clear by specifying return types!」

---

## 📺 Code for Display

```typescript
/** Example 1: void type - doesn't use return value */
function log(message: string): void {
  console.log(message);
  // return undefined; is implicit
}

/** Example 2: undefined type - explicitly returns undefined */
function find(): User | undefined {
  return undefined;
}

/** Example 3: Implicit undefined */
function noReturn() {
  // Returns nothing
}
const result = noReturn(); // undefined
```
