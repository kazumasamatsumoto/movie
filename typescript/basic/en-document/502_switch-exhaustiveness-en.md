# #502 "Switch Exhaustiveness"

Shikoku Metan: "Let's verify exhaustiveness with switch statements."
Zundamon: "handleAction() covered create, update, and delete."
Shikoku Metan: "Dropping const exhaustive: never = action; in default keeps us safe."
Zundamon: "A shared assertNever() helper is handy."
Shikoku Metan: "process() or any other switch can reuse the same guard."
Zundamon: "When the Status union forgets 'success', assertNever(status) complains."
Shikoku Metan: "You instantly notice when the union grows."
Zundamon: "Let the default branch act as the watchdog."

---

## 📺 Code for Display

```typescript
/** Example 1: Exhaustive Action switch */
type Action = "create" | "update" | "delete";

function handleAction(action: Action): void {
  switch (action) {
    case "create":
      console.log("Creating");
      break;
    case "update":
      console.log("Updating");
      break;
    case "delete":
      console.log("Deleting");
      break;
    default:
      const exhaustive: never = action;
      throw new Error(`Unhandled: ${exhaustive}`);
  }
}

/** Example 2: Reusable assertNever */
function assertNever(value: never): never {
  throw new Error(`Unhandled case: ${value}`);
}

function process(action: Action): void {
  switch (action) {
    case "create":
      return;
    case "update":
      return;
    case "delete":
      return;
    default:
      assertNever(action);
  }
}

/** Example 3: Status guard */
type Status = "idle" | "loading" | "success";

function handle(status: Status): void {
  switch (status) {
    case "idle":
      return;
    case "loading":
      return;
    case "success":
      return;
    default:
      assertNever(status);
  }
}
```
