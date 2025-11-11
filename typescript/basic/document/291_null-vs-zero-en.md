# #291 "Differences Between null and 0"

Shikoku Metan「Let's learn about the differences between null and 0!」
Zundamon「They both feel like nothing, but are they different?」
Shikoku Metan「Yes. null is null type, 0 is number type - they have different types.」
Zundamon「null === 0 becomes false!」
Shikoku Metan「Exactly. They also behave differently with Nullish Coalescing.」
Zundamon「0 doesn't get replaced by the ?? operator because it's a valid number?」
Shikoku Metan「Yes. 0 is a valid value, so null ?? 10 is 10, but 0 ?? 10 is 0.」
Zundamon「Use Union types explicitly to maintain type safety!」

---

## 📺 Code for Display

```typescript
/** Example 1: Type differences */
let a: null = null;   // null type
let b: number = 0;    // number type
null === 0;  // false

/** Example 2: Nullish Coalescing behavior */
const count1 = null ?? 10;  // 10
const count2 = 0 ?? 10;     // 0 (0 is a valid value)

/** Example 3: Type safety */
// let num: number = null;  // Error
let num: number | null = null;  // OK
```
