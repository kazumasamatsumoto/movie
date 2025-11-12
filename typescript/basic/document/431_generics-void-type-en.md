# #431 "void in Generics"

Shikoku Metan: "Generics can incorporate void types as well."
Zundamon: "We defined Callback<T> = (value: T) => void earlier."
Shikoku Metan: "Passing number yields a side-effect handler for numbers."
Zundamon: "Can Promise<T> also use void?"
Shikoku Metan: "Yes, declare saveData(): Promise<void>."
Zundamon: "Handler<User> = (data: User) => void is another staple."
Shikoku Metan: "Generics plus void make reusable side-effect handlers."
Zundamon: "I'll design flexible void handlers!"

---

## 📺 Code for Display

```typescript
/** Example 1: Generic void callback */

type Callback<T> = (value: T) => void;
const numberCallback: Callback<number> = (n) => {
  console.log(n);
};

/** Example 2: Promise<void> */

async function saveData(): Promise<void> {
  await database.save();
}

/** Example 3: Generic handler */

type Handler<T> = (data: T) => void;
const userHandler: Handler<User> = (user) => {
  console.log(user.name);
};
```
