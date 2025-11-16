# #356 "Difference Between ?? and ||"

Shikoku Metan: "Understand the difference between ?? and ||."
Zundamon: "|| treats 0 or empty strings as falsy and overwrites them, right?"
Shikoku Metan: "Yes, while ?? targets only null and undefined."
Zundamon: "So keeping a volume of 0 requires ??"
Shikoku Metan: "Exactly; volume ?? 50 preserves zero as a valid value."
Zundamon: "Can it also keep boolean false?"
Shikoku Metan: "Yes, enabled ?? true respects false flags and only replaces nullish ones."
Zundamon: "Whenever falsy still matters, I'll reach for ??!"

---

## 📺 Code for Display

```typescript
/** Example 1: Comparing ?? and || */
const count1 = 0 || 10;   // 10 (0 is falsy)
const count2 = 0 ?? 10;   // 0  (0 isn't nullish)

const text1 = "" || "default";   // "default"
const text2 = "" ?? "default";   // ""

/** Example 2: Applying it to numeric defaults */
function setVolume(volume: number | null | undefined) {
  const vol = volume ?? 50;  // 0 is a valid volume
  console.log(`Volume: ${vol}`);
}

/** Example 3: Applying it to boolean defaults */
const enabled = config.enabled ?? true;  // false is valid
const verbose = options.verbose ?? false;
```
