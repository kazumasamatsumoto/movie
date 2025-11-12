# #388 "return undefined"

Shikoku Metan: "return undefined; is allowed in void functions."
Zundamon: "So log1 can write it without errors."
Shikoku Metan: "Right, though log2 and log3 show that return; or no return is cleaner."
Zundamon: "Early returns like if (!value) return; are recommended too?"
Shikoku Metan: "Exactly—validate demonstrates that pattern."
Zundamon: "I'll choose between returning undefined and plain return based on style guides."
Shikoku Metan: "Both are fine as long as the team agrees."
Zundamon: "Now I get the return styles for void functions!"

---

## 📺 Code for Display

```typescript
/** Example 1: return undefined */
function log1(msg: string): void {
  console.log(msg);
  return undefined;
}

/** Example 2: Preferred style */
function log2(msg: string): void {
  console.log(msg);
  return;
}
function log3(msg: string): void {
  console.log(msg);
}

/** Example 3: Early return */
function validate(value: string): void {
  if (!value) return;
  console.log(value);
}
```
