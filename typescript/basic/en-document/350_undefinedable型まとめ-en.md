# #350 "Undefinedable Types Summary"

Shikoku Metan: "Let's summarize undefinedable types!"
Zundamon: "With T | undefined, we can create types that allow undefined!"
Shikoku Metan: "Yes. Optional properties automatically become undefinedable."
Zundamon: "There are several safe access methods, right?"
Shikoku Metan: "Exactly. We can use Optional Chaining and the Nullish Coalescing operator."
Zundamon: "How do we use them in practical patterns?"
Shikoku Metan: "Yes. It's useful to combine with default values, like options?.port ?? 8080."
Zundamon: "By mastering undefinedable types, we can write robust code!"

---

## 📺 Code for Display

```typescript
/** Example 1: Undefinedable type basics */
type Undefinedable<T> = T | undefined;
interface User {
  name: string;
  age?: number;  // Optional
}

/** Example 2: Safe access */
function greet(user?: User) {
  const name = user?.name ?? "Guest";
  console.log(`Hello, ${name}`);
}

/** Example 3: Practical pattern */
const config: Config = {
  host: "localhost",
  port: options?.port ?? 8080,
  timeout: options?.timeout ?? 3000,
};
```
