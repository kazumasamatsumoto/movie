# #501 "What Is Exhaustive Checking"

Shikoku Metan: "Time to review the basics of exhaustive checking."
Zundamon: "It means covering every literal like the Status union."
Shikoku Metan: "A default branch that treats a never status exposes gaps fast."
Zundamon: "incomplete() forgot the 'error' case and TypeScript yelled."
Shikoku Metan: "Writing const exhaustive: never = status; keeps the type system on patrol."
Zundamon: "Color unions can throw via assertNever() when something is missing."
Shikoku Metan: "Crashing builds the moment we add colors feels safe."
Zundamon: "Let exhaustive checks brace us for spec changes."

---

## 📺 Code for Display

```typescript
/** Example 1: Exhaustive handleStatus */
type Status = "pending" | "success" | "error";

function handleStatus(status: Status): void {
  switch (status) {
    case "pending":
      console.log("Pending");
      break;
    case "success":
      console.log("Success");
      break;
    case "error":
      console.log("Error");
      break;
    default:
      const exhaustive: never = status;
      throw new Error(`Unhandled: ${exhaustive}`);
  }
}

/** Example 2: Detecting missing cases */
function incomplete(status: Status): void {
  switch (status) {
    case "pending":
      console.log("Pending");
      break;
    case "success":
      console.log("Success");
      break;
    default:
      const exhaustive: never = status;
      throw new Error(`Missing case: ${exhaustive}`);
  }
}

/** Example 3: Color union with assertNever */
type Color = "red" | "blue" | "green";

function assertNever(value: never): never {
  throw new Error(`Unhandled color: ${value}`);
}

function getHex(color: Color): string {
  switch (color) {
    case "red":
      return "#ff0000";
    case "blue":
      return "#0000ff";
    case "green":
      return "#00ff00";
    default:
      return assertNever(color);
  }
}
```
