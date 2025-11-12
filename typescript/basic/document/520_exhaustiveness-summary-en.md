# #520 "Exhaustiveness Recap"

Shikoku Metan: "Let's wrap the never series with an exhaustiveness recap."
Zundamon: "handle() covered pending, success, and error."
Shikoku Metan: "Dropping return exhaustiveCheck(status); makes future additions fail fast."
Zundamon: "process() on Result chose the value or threw the error via the ok flag."
Shikoku Metan: "EventHandler switched over click and keypress, then defaulted to exhaustiveCheck(event)."
Zundamon: "Master these three patterns and most unions feel familiar."
Shikoku Metan: "With never on our side we're ready for spec changes."
Zundamon: "Time to evangelize exhaustiveness checks!"

---

## 📺 Code for Display

```typescript
/** Example 1: Basic form */
type Status = "pending" | "success" | "error";

function exhaustiveCheck(value: never): never {
  throw new Error(`Unhandled: ${value}`);
}

function handle(status: Status): string {
  if (status === "pending") return "Processing";
  if (status === "success") return "Done";
  if (status === "error") return "Failed";
  return exhaustiveCheck(status);
}

/** Example 2: Result type */
type Result<T, E> =
  | { ok: true; value: T }
  | { ok: false; error: E };

function process<T, E>(result: Result<T, E>): T {
  if (result.ok) return result.value;
  if (!result.ok) throw result.error;
  return exhaustiveCheck(result);
}

/** Example 3: Event handling */
type Event =
  | { type: "click"; x: number; y: number }
  | { type: "keypress"; key: string };

class EventHandler {
  handle(event: Event): void {
    switch (event.type) {
      case "click":
        return this.onClick(event.x, event.y);
      case "keypress":
        return this.onKey(event.key);
      default:
        return exhaustiveCheck(event);
    }
  }

  private onClick(x: number, y: number) {
    console.log("click", x, y);
  }

  private onKey(key: string) {
    console.log("key", key);
  }
}
```
