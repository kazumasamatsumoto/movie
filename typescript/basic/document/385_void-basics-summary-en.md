# #385 "Basics Summary"

Shikoku Metan: "Let's recap the essentials of void."
Zundamon: "Functions like log represent the typical side-effect pattern."
Shikoku Metan: "Right—they finish work without producing values."
Zundamon: "Remember that Promise<void> applies to async flows too!"
Shikoku Metan: "saveData only signals completion in that case."
Zundamon: "And Callback = (data: string) => void defines handler types cleanly."
Shikoku Metan: "Side-effect-specific aliases boost readability."
Zundamon: "Master the basics to wield void confidently!"

---

## 📺 Code for Display

```typescript
/** Example 1: Void basics */
function log(msg: string): void {
  console.log(msg);
}

/** Example 2: Promise<void> */
async function saveData(data: Data): Promise<void> {
  await database.save(data);
}

/** Example 3: Practical pattern */
type Callback = (data: string) => void;
const handler: Callback = (data) => {
  console.log(data);
};
```
