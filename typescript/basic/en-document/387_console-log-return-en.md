# #387 "Return Value of console.log"

Shikoku Metan: "console.log is also a void-returning function."
Zundamon: "Assigning result = console.log('Hello') gives result the void type, right?"
Shikoku Metan: "Exactly; it isn't meant to produce usable values."
Zundamon: "logAndReturn trying to return console.log as a string triggers an error?"
Shikoku Metan: "Yes—Type 'void' is not assignable to type 'string'."
Zundamon: "The process function uses console.log purely for side effects, which is correct."
Shikoku Metan: "Remember that console.log is designed solely for side effects."
Zundamon: "I won't misuse APIs whose return type is void!"

---

## 📺 Code for Display

```typescript
/** Example 1: console.log signature */
const result = console.log("Hello");
// result: void

/** Example 2: Do not use the return */
function logAndReturn(msg: string): string {
  return console.log(msg);  // Error
}

/** Example 3: Proper usage */
function process(data: Data): void {
  console.log("Processing:", data);
}
```
