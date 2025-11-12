# #511 "Type Guards"

Shikoku Metan: "Let's narrow unions with type guards."
Zundamon: "area() on Shape inspected kind to compute each area."
Shikoku Metan: "Listing circle, square, rectangle plus const check: never = shape seals it."
Zundamon: "A custom isCircle() guard boosts readability."
Shikoku Metan: "process() narrows to radius as soon as isCircle(shape) passes."
Zundamon: "The remaining shapes can route to other logic for maintenance."
Shikoku Metan: "Consistent guards also make exhaustive checks easier."
Zundamon: "Even growing unions feel safer this way."

---

## 📺 Code for Display

```typescript
/** Example 1: Compute area via kind */
type Shape =
  | { kind: "circle"; radius: number }
  | { kind: "square"; size: number }
  | { kind: "rectangle"; width: number; height: number };

function area(shape: Shape): number {
  if (shape.kind === "circle") {
    return Math.PI * shape.radius ** 2;
  } else if (shape.kind === "square") {
    return shape.size ** 2;
  } else if (shape.kind === "rectangle") {
    return shape.width * shape.height;
  }
  const check: never = shape;
  throw new Error(`Unhandled: ${JSON.stringify(check)}`);
}

/** Example 2: Custom guard */
function isCircle(shape: Shape): shape is Extract<Shape, { kind: "circle" }> {
  return shape.kind === "circle";
}

/** Example 3: Using the guard */
function process(shape: Shape): number {
  if (isCircle(shape)) {
    return shape.radius;
  }
  // Remaining shapes handled here
  return area(shape);
}
```
