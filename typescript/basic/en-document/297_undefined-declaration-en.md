# #297 "Undefined Declaration"

Shikoku Metan「Let's learn about undefined declaration!」
Zundamon「How do we declare it?」
Shikoku Metan「Yes. We can declare with undefined type or Union types.」
Zundamon「name?: string is an optional property!」
Shikoku Metan「Exactly. It's optional and means the same as string | undefined.」
Zundamon「Can we use it for function parameters?」
Shikoku Metan「Yes. Function parameters can also be made optional.」
Zundamon「Setting default values with ?? operator is convenient!」

---

## 📺 Code for Display

```typescript
/** Example 1: undefined type declaration */
let value: undefined = undefined;
let name: string | undefined;

/** Example 2: Optional properties */
interface User {
  name?: string;  // string | undefined
  age?: number;   // number | undefined
}

/** Example 3: Function parameters */
function greet(name?: string): void {
  console.log(name ?? "Guest");
}
```
