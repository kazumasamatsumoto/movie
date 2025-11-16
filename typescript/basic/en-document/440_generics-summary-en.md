# #440 "Generics Summary"

Shikoku Metan: "Let's wrap up void plus generics."
Zundamon: "Callback<User> builds side-effect handlers with type parameters."
Shikoku Metan: "Handler<T = void> adds helpful defaults."
Zundamon: "EventEmitter<T = void> is another great template."
Shikoku Metan: "Combining void with generics boosts extensibility."
Zundamon: "I'll design reusable APIs using this summary!"

---

## 📺 Code for Display

```typescript
/** Example 1: Basic generic */

type Callback<T> = (data: T) => void;
const handler: Callback<User> = (user) => {
  console.log(user.name);
};

/** Example 2: Default parameter */

type Handler<T = void> = (data: T) => void;
const voidHandler: Handler = () => {
  console.log("Done");
};

/** Example 3: Practical example */

class EventEmitter<T = void> {
  on(listener: (data: T) => void): void {}
}
```
