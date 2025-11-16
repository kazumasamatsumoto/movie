# #255 "Comparison Operations Summary"

Shikoku Metan: "Let's learn the summary of comparison operations!"
Zundamon: "We're organizing what we've learned so far!"
Shikoku Metan: "Yes. First, we recommend using the strict equality operator ===."
Zundamon: "We needed to be careful with floating-point comparisons, right!"
Shikoku Metan: "Exactly. Use the isClose function to set a tolerance."
Zundamon: "We should explicitly check null and undefined!"
Shikoku Metan: "For range checks, combine >= and <=."
Zundamon: "Follow best practices and write type-safe code!"

---

## 📺 Code for Display

```typescript
/** Example 1: Recommended: Use === */
if (value === 0) { }

/** Example 2: Floating-point comparison */
function isClose(a: number, b: number): boolean {
  return Math.abs(a - b) < 1e-10;
}

/** Example 3: null/undefined check and range check */
if (value === null) { }
if (value === undefined) { }

// Range check
if (score >= 60 && score <= 100) { }
```
