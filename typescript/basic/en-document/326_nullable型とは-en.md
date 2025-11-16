# #326 "What is Nullable Type - T | null"

Shikoku Metan: "Let's learn about nullable types!"
Zundamon: "Nullable types are types that allow null!"
Shikoku Metan: "That's right. Using the T | null format, we can express the possibility of a null value."
Zundamon: "It's convenient for function return values when returning null for not found cases, right?"
Shikoku Metan: "Exactly. By using User | null, we can explicitly indicate the possibility of non-existence."
Zundamon: "We can use nullable types in properties too!"
Shikoku Metan: "Yes. They're ideal for representing optional services and configuration values."
Zundamon: "With nullable types, we can create more accurate type definitions!"

---

## 📺 Code for Display

```typescript
/** Example 1: Nullable type basics */
type Nullable<T> = T | null;
let name: Nullable<string> = null;
let age: number | null = 25;

/** Example 2: Function return values */
function findUser(id: number): User | null {
  return users.find(u => u.id === id) ?? null;
}

/** Example 3: Properties */
interface Config {
  cache: CacheService | null;
  logger: Logger | null;
}
```
