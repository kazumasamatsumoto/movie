# #433 "Callback<void>"

Shikoku Metan: "Callback<void> expresses pure side-effect callbacks."
Zundamon: "onComplete was just () => console.log."
Shikoku Metan: "EventHandler<T = void> keeps handlers type-safe."
Zundamon: "Async callbacks fit AsyncCallback<T> that returns Promise<void>?"
Shikoku Metan: "Exactly—saveCallback shows that pattern."
Zundamon: "We can mix synchronous and async void callbacks as needed."
Shikoku Metan: "It's perfect for simple side-effect APIs."
Zundamon: "I'll keep the Callback<void> idiom handy!"

---

## 📺 Code for Display

```typescript
/** Example 1: Defining callbacks */

type Callback<T> = (data: T) => void;
type VoidCallback = Callback<void>;
const onComplete: VoidCallback = () => {
  console.log("Complete");
};

/** Example 2: Event handler */

type EventHandler<T = void> = (event: T) => void;
const clickHandler: EventHandler<MouseEvent> = (e) => {
  console.log(e.clientX);
};

/** Example 3: Async callback */

type AsyncCallback<T> = (data: T) => Promise<void>;
const saveCallback: AsyncCallback<User> = async (user) => {
  await database.save(user);
};
```
