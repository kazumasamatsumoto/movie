# #435 "Mapped Types"

Shikoku Metan: "Mapped Types can convert every method to void."
Zundamon: "VoidMethods<Service> forced all returns to void for mocking."
Shikoku Metan: "Exactly; handy for test doubles."
Zundamon: "ToHandlers<T> turned properties into (value: T[K]) => void handlers."
Shikoku Metan: "Great for assigning handlers per property."
Zundamon: "So Mapped Types let us automate void conversions."
Shikoku Metan: "Combine them with generics for flexible transformations."
Zundamon: "I'll leverage void-focused mapped types!"

---

## 📺 Code for Display

```typescript
/** Example 1: Make every method void */

type VoidMethods<T> = {
  [K in keyof T]: T[K] extends (...args: any[]) => any
    ? (...args: Parameters<T[K]>) => void
    : T[K];
};

/** Example 2: Practical use */

interface Service {
  getData(): Promise<Data>;
  saveData(data: Data): Promise<void>;
}
type MockService = VoidMethods<Service>;

/** Example 3: Convert properties to handlers */

type ToHandlers<T> = {
  [K in keyof T]: (value: T[K]) => void;
};
type UserHandlers = ToHandlers<User>;
```
