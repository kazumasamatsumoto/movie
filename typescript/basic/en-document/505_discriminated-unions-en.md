# #505 "Discriminated Unions"

Shikoku Metan: "Discriminated unions branch on kind or type fields."
Zundamon: "Shape.getArea() computed the area per kind."
Shikoku Metan: "A default assertNever(shape) keeps new figures safe."
Zundamon: "Redux-style Action unions rely on type inside the reducer."
Shikoku Metan: "increment, decrement, and set all lead to assertNever(action) afterward."
Zundamon: "The Event handler logged click and keypress events."
Shikoku Metan: "As soon as we add a type, handleEvent() turns red."
Zundamon: "Discriminated unions are a powerhouse for missing-branch detection."

---

## 📺 Code for Display

```typescript
/** Example 1: Shape areas */
type Circle = { kind: "circle"; radius: number };
type Square = { kind: "square"; size: number };
type Triangle = { kind: "triangle"; base: number; height: number };
type Shape = Circle | Square | Triangle;

function assertNever(value: never): never {
  throw new Error(`Unhandled: ${JSON.stringify(value)}`);
}

function getArea(shape: Shape): number {
  switch (shape.kind) {
    case "circle":
      return Math.PI * shape.radius ** 2;
    case "square":
      return shape.size ** 2;
    case "triangle":
      return (shape.base * shape.height) / 2;
    default:
      return assertNever(shape);
  }
}

/** Example 2: Redux-style reducer */
type Action =
  | { type: "increment" }
  | { type: "decrement" }
  | { type: "set"; payload: number };

function reducer(state: number, action: Action): number {
  switch (action.type) {
    case "increment":
      return state + 1;
    case "decrement":
      return state - 1;
    case "set":
      return action.payload;
    default:
      return assertNever(action);
  }
}

/** Example 3: Event handling */
type Event =
  | { type: "click"; x: number; y: number }
  | { type: "keypress"; key: string };

function handleEvent(event: Event): void {
  switch (event.type) {
    case "click":
      console.log(`Clicked at ${event.x}, ${event.y}`);
      break;
    case "keypress":
      console.log(`Key: ${event.key}`);
      break;
    default:
      assertNever(event);
  }
}
```
