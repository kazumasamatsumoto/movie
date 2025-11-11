# #309 "undefined Patterns"

Shikoku Metan: "Let's learn about practical patterns using undefined!"
Zundamon: "With the Option type pattern, we can express the possibility of missing values through types!"
Shikoku Metan: "That's right. The union type T | undefined enables safe value handling."
Zundamon: "The default value pattern can be written concisely using the nullish coalescing operator ??, right?"
Shikoku Metan: "Exactly. It allows setting fallback values for undefined cases."
Zundamon: "The Partial type pattern is convenient for making all properties optional!"
Shikoku Metan: "Using these patterns makes error handling type-safe."
Zundamon: "With Option and Partial types, we can effectively utilize undefined!"

---

## 📺 Code for Display

```typescript
/** Example 1: Option type pattern */
type Option<T> = T | undefined;
function divide(a: number, b: number): Option<number> {
  return b !== 0 ? a / b : undefined;
}

/** Example 2: Default value pattern */
function greet(name?: string): void {
  const displayName = name ?? "Guest";
  console.log(`Hello, ${displayName}`);
}

/** Example 3: Partial type pattern */
interface User {
  name: string;
  age: number;
}
type PartialUser = Partial<User>;
// { name?: string; age?: number }
```
