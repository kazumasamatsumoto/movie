# #515 "Compiler Optimizations"

Shikoku Metan: "Never checks can serve as optimization hints."
Zundamon: "isEven() covered every Digit via switch."
Shikoku Metan: "Putting const check: never = n; in default marks code as unreachable."
Zundamon: "getScore() removed dead paths even with simple if chains."
Shikoku Metan: "Bool.not() flipped true/false then threw, encouraging inlining."
Zundamon: "Treating the rest as never eliminates redundant returns."
Shikoku Metan: "Telling the compiler 'we never get here' can speed things up."
Zundamon: "It's nice when type safety and optimization align."

---

## 📺 Code for Display

```typescript
/** Example 1: Even digits */
type Digit = 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9;

function isEven(n: Digit): boolean {
  switch (n) {
    case 0:
    case 2:
    case 4:
    case 6:
    case 8:
      return true;
    case 1:
    case 3:
    case 5:
    case 7:
    case 9:
      return false;
    default:
      const check: never = n;
      return false;
  }
}

/** Example 2: Priority scores */
type Priority = "high" | "medium" | "low";

function getScore(p: Priority): number {
  if (p === "high") return 3;
  if (p === "medium") return 2;
  if (p === "low") return 1;
  const check: never = p;
  return 0;
}

/** Example 3: Boolean negate */
type Bool = true | false;

function not(b: Bool): boolean {
  if (b === true) return false;
  if (b === false) return true;
  const check: never = b;
  throw new Error(`Invalid: ${check}`);
}
```
