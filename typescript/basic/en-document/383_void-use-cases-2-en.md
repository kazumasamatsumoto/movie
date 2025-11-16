# #383 "Use Cases"

Shikoku Metan: "Let's summarize common void use cases."
Zundamon: "Event handlers typically look like (e: Event): void => { ... }."
Shikoku Metan: "Right, the signature shows the handler doesn't return anything."
Zundamon: "Callbacks in array.forEach can also be void if they only log?"
Shikoku Metan: "Exactly—they perform side effects only."
Zundamon: "Middleware types even include next: () => void!"
Shikoku Metan: "Yes, the Middleware type itself returns void and passes control via next."
Zundamon: "I'll tailor void usage to each scenario!"

---

## 📺 Code for Display

```typescript
/** Example 1: Event handler */
button.addEventListener("click", (e: Event): void => {
  console.log("Clicked");
});

/** Example 2: Callback function */
array.forEach((item: string): void => {
  console.log(item);
});

/** Example 3: Middleware */
type Middleware = (
  req: Request,
  res: Response,
  next: () => void
) => void;
```
