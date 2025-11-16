# #342 "Declaring Undefinedable Types"

Shikoku Metan「Let's learn how to declare undefinedable types!」
Zundamon「The basic declaration is type | undefined!」
Shikoku Metan「Yes. We can directly specify T | undefined for variables.」
Zundamon「Can we reuse it with type aliases?」
Shikoku Metan「Exactly. We can create a common pattern with generic types like Undefinedable<T>.」
Zundamon「We can use it in interfaces too!」
Shikoku Metan「Yes. We can specify T | undefined as a property type.」
Zundamon「By declaring undefinedable types, we can create flexible type definitions!」

---

## 📺 Code for Display

```typescript
/** Example 1: Basic declaration */
let value: string | undefined;
let count: number | undefined = undefined;
let flag: boolean | undefined;

/** Example 2: Reuse with type alias */
type Undefinedable<T> = T | undefined;
let name: Undefinedable<string>;
let age: Undefinedable<number>;

/** Example 3: Using in interfaces */
interface Config {
  timeout: number | undefined;
  maxRetries: number | undefined;
  callback: ((data: string) => void) | undefined;
}
```
