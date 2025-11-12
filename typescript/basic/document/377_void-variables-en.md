# #377 "void Variables"

Shikoku Metan: "Let's also mention variables typed as void."
Zundamon: "We can write let value: void;, but it's rarely useful, right?"
Shikoku Metan: "Correct; only undefined fits, and strictNullChecks forbids null."
Zundamon: "Can I store the result of execute(): void in a void variable?"
Shikoku Metan: "Sure—const result: void = execute(); matches the signature."
Zundamon: "Managing arrays of void callbacks seems handy though!"
Shikoku Metan: "A VoidCallback[] lets you queue side-effect-only handlers."
Zundamon: "Knowing this keeps me from getting confused by the type system!"

---

## 📺 Code for Display

```typescript
/** Example 1: A void variable */
let value: void;
value = undefined;  // OK
// value = null;    // Error under strictNullChecks

/** Example 2: Treating a return value as void */
function execute(): void {
  console.log("Executed");
}
const result: void = execute();

/** Example 3: Practical callback list */
type VoidCallback = () => void;
const callbacks: VoidCallback[] = [];
callbacks.push(() => console.log("Done"));
```
