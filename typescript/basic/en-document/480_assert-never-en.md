# #480 "assertNever Function"

Shikoku Metan: "Finally, let's review assertNever functions."
Zundamon: "They always throw for unexpected cases."
Shikoku Metan: "handleStatus and getColor used them for exhaustiveness."
Zundamon: "Adding new Color values surfaces compile errors."
Shikoku Metan: "Keep assertNever as a final safety net."

---

## 📺 Code for Display

```typescript
/** Example 1: Definition */
function assertNever(value: never): never {
  throw new Error(`Unexpected value: ${value}`);
}

/** Example 2: Status handling */
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
      assertNever(status);
  }
}

/** Example 3: Detect new types */
type Color = "red" | "blue" | "green";
function getColor(color: Color): string {
  switch (color) {
    case "red": return "#ff0000";
    case "blue": return "#0000ff";
    default: return assertNever(color);
  }
}
```
