# #404 "Assigning undefined"

Shikoku Metan: "Only undefined may be assigned to a void variable."
Zundamon: "We saw value: void = undefined earlier."
Shikoku Metan: "Right, strictNullChecks even forbids null."
Zundamon: "An undefined-typed variable accepts nothing else?"
Shikoku Metan: "Exactly."
Zundamon: "In practice we often store the return of void functions instead?"
Shikoku Metan: "Calling doSomething(): void produces undefined, so the assignment lines up."
Zundamon: "I'll follow those rules to dodge type errors!"

---

## 📺 Code for Display

```typescript
/** Example 1: void variable */
let value: void;
value = undefined;  // OK

/** Example 2: undefined variable */
let undef: undefined;
undef = undefined;  // OK

/** Example 3: Treat function return */
function doSomething(): void {
  console.log("Done");
}
const result: void = doSomething();
```
