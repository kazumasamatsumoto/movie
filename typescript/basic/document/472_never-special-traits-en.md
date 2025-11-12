# #472 "Special Traits"

Shikoku Metan: "never behaves uniquely in unions and intersections."
Zundamon: "string | never simplifying to string shows that."
Shikoku Metan: "Whereas string & never collapses to never."
Zundamon: "We also built exhaustiveCheck(value: never) for switch statements."
Shikoku Metan: "It caught missing Color cases."
Zundamon: "I will leverage these traits for safer types!"

---

## 📺 Code for Display

```typescript
/** Example 1: Union & intersection */
type Result1 = string | never;
type Result4 = string & never;

/** Example 2: Exhaustive check function */
function exhaustiveCheck(value: never): never {
  throw new Error(`Unhandled case: ${value}`);
}

/** Example 3: Usage example */
type Color = "red" | "blue";
function getColor(color: Color): string {
  if (color === "red") return "#ff0000";
  if (color === "blue") return "#0000ff";
  return exhaustiveCheck(color);
}
```
