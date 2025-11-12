# #510 "Practical Example (2)"

Shikoku Metan: "Practical example two dives into event-driven apps."
Zundamon: "DomainEvent offered UserCreated, UserUpdated, and UserDeleted."
Shikoku Metan: "EventHandler.handle() branched with if-else and ended in exhaustiveCheck(event)."
Zundamon: "Even with separate methods we still remembered the never guard."
Shikoku Metan: "The API response union switched on the status field."
Zundamon: "process() returned data for success and threw on error."
Shikoku Metan: "const check: never = res; exposes new status additions immediately."
Zundamon: "Real-world unions feel sturdier once never protects them."

---

## 📺 Code for Display

```typescript
/** Example 1: Domain events */
type DomainEvent =
  | { type: "UserCreated"; userId: string }
  | { type: "UserUpdated"; userId: string; data: unknown }
  | { type: "UserDeleted"; userId: string };

/** Example 2: Event handler class */
class EventHandler {
  handle(event: DomainEvent): void {
    if (event.type === "UserCreated") this.onCreate(event);
    else if (event.type === "UserUpdated") this.onUpdate(event);
    else if (event.type === "UserDeleted") this.onDelete(event);
    else this.exhaustiveCheck(event);
  }

  private onCreate(event: Extract<DomainEvent, { type: "UserCreated" }>) {
    console.log("User created", event.userId);
  }

  private onUpdate(event: Extract<DomainEvent, { type: "UserUpdated" }>) {
    console.log("User updated", event.userId, event.data);
  }

  private onDelete(event: Extract<DomainEvent, { type: "UserDeleted" }>) {
    console.log("User deleted", event.userId);
  }

  private exhaustiveCheck(value: never): never {
    throw new Error(`Unhandled: ${value}`);
  }
}

/** Example 3: API responses */
type ApiResponse<T> =
  | { status: "success"; data: T }
  | { status: "error"; error: string };

function process<T>(res: ApiResponse<T>) {
  if (res.status === "success") return res.data;
  if (res.status === "error") throw new Error(res.error);
  const check: never = res;
  return check;
}
```
