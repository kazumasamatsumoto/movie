# #407 "Return Type undefined"

Shikoku Metan: "Functions returning undefined produce that value explicitly."
Zundamon: "getOptionalValue returns either 42 or undefined."
Shikoku Metan: "Right, so callers must check for undefined."
Zundamon: "The difference from void is whether the value is used?"
Shikoku Metan: "Exactly—void is for side effects, undefined is data."
Zundamon: "undefFunc even returns undefined explicitly."
Shikoku Metan: "While voidFunc simply logs and stops."
Zundamon: "I'll choose return types based on that distinction!"

---

## 📺 Code for Display

```typescript
/** Example 1: Function returning undefined */
function getOptionalValue(): number | undefined {
  if (Math.random() > 0.5) {
    return 42;
  }
  return undefined;
}

/** Example 2: Check before using */
const value = getOptionalValue();
if (value !== undefined) {
  console.log(value * 2);
}

/** Example 3: Difference from void */
function voidFunc(): void {
  console.log("Done");
}
function undefFunc(): undefined {
  return undefined;
}
```
