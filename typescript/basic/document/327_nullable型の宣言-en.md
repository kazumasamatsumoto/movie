# #327 "Declaring Nullable Types"

Shikoku Metan: "Let's learn how to declare nullable types!"
Zundamon: "There's a way to declare them directly!"
Shikoku Metan: "Yes. You can declare them as a union type, like string | null."
Zundamon: "Using type aliases makes them reusable and convenient, right?"
Shikoku Metan: "Exactly. By defining Nullable<T> = T | null, you can use it generically."
Zundamon: "They can be used in interface properties too!"
Shikoku Metan: "Yes. Like ApiResponse, you can make data and error nullable."
Zundamon: "Choose the appropriate declaration method based on the use case!"

---

## 📺 Code for Display

```typescript
/** Example 1: Direct declaration */
let name: string | null = null;
let age: number | null = null;

/** Example 2: Type alias */
type Nullable<T> = T | null;
let user: Nullable<User> = null;
let config: Nullable<Config> = null;

/** Example 3: Interface */
interface ApiResponse<T> {
  data: T | null;
  error: string | null;
}
```
