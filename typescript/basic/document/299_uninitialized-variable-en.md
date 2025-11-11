# #299 "Uninitialized Variables"

Shikoku Metan「Let's learn about uninitialized variables!」
Zundamon「Variables that are only declared without a value?」
Shikoku Metan「Yes. In that case, the variable's value is undefined.」
Zundamon「console.log shows undefined!」
Shikoku Metan「Exactly. In strict mode, initialization may be required.」
Zundamon「Do we explicitly set undefined to prevent errors?」
Shikoku Metan「Yes. Declare with Union types and check appropriately.」
Zundamon「It's safe to check with !== undefined before using!」

---

## 📺 Code for Display

```typescript
/** Example 1: Uninitialized variable */
let name: string | undefined;
console.log(name); // undefined

/** Example 2: Error in strict mode */
// let id: number; // Error: Initialization required
// id = 42;  // OK

/** Example 3: Explicit undefined */
let value: string | undefined = undefined;
if (value !== undefined) {
  console.log(value.toUpperCase());
}
```
