# #381 "Type Inference"

Shikoku Metan: "The void type is often inferred from a function body."
Zundamon: "Does function log1(msg: string) get void automatically?"
Shikoku Metan: "Yes, without a return statement the compiler infers void."
Zundamon: "Still, adding : void helps communicate intent for some APIs, right?"
Shikoku Metan: "Exactly—log2 shows how an annotation reassures readers of a public API."
Zundamon: "Will an arrow like (e: Event) => { ... } also become => void automatically?"
Shikoku Metan: "It does; handler becomes (Event) => void as long as it returns nothing."
Zundamon: "I'll balance inference and explicit types when using void!"

---

## 📺 Code for Display

```typescript
/** Example 1: Void inferred automatically */
function log1(msg: string) {
  console.log(msg);
  // Return type inferred as void
}

/** Example 2: Explicit void */
function log2(msg: string): void {
  console.log(msg);
  // Intent is explicit
}

/** Example 3: Relying on inference */
const handler = (e: Event) => {
  console.log(e);
};  // Inferred as (e: Event) => void
```
