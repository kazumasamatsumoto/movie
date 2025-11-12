# #534 "Type Inference Relationships"

Shikoku Metan: "Never plays tightly with inference."
Zundamon: "In process(), once we handle string/number the leftover value becomes never."
Shikoku Metan: "Type guards on Shape let the other branch infer automatically."
Zundamon: "Handle circle first and the else block knows it's square."
Shikoku Metan: "Conditional helpers like InferReturnType<T> pull return types from functions."
Zundamon: "Functions infer cleanly; non-functions fall back to never."
Shikoku Metan: "Inference plus never produces great IDE hints."
Zundamon: "Let types narrate your intent."

---

## 📺 Code for Display

```typescript
/** Example 1: Control-flow inference */
function process(value: string | number) {
  if (typeof value === "string") {
    return value.toUpperCase();
  } else if (typeof value === "number") {
    return value * 2;
  }
  const check: never = value;
}
```

```typescript
/** Example 2: Type guards */
type Shape = { kind: "circle" } | { kind: "square" };

function handle(shape: Shape) {
  if (shape.kind === "circle") {
    // shape is circle
  } else {
    // shape is square
  }
}
```

```typescript
/** Example 3: InferReturnType */
type InferReturnType<T> =
  T extends (...args: any[]) => infer R ? R : never;

type R1 = InferReturnType<() => string>; // string
type R2 = InferReturnType<string>;       // never
```
