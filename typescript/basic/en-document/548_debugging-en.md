# #548 "Debugging"

Shikoku Metan: "Debug never-related errors step by step."
Zundamon: "Step 1 is to read the compiler message."
Shikoku Metan: "If Action = 'create' | 'update' | 'delete' and you only handle 'create', you still have 'update' | 'delete'."
Zundamon: "Step 2 hovers action in VSCode to see the remaining union."
Shikoku Metan: "Handle update/delete, then drop const check: never = action;."
Zundamon: "Step 3 uses a debugNever() helper for runtime logging."
Shikoku Metan: "It prints 'Unhandled case in process: ...' before throwing."
Zundamon: "Follow the error → inspect remaining cases → helper pattern."

---

## 📺 Code for Display

```typescript
/** Example 1: Inspect type errors */
type Action = "create" | "update" | "delete";

function handle(action: Action): string {
  if (action === "create") return "Created";
  const check: never = action;
  return "";
}
```

```typescript
/** Example 2: Handle the rest */
function handleFixed(action: Action): string {
  if (action === "create") return "Created";
  if (action === "update") return "Updated";
  if (action === "delete") return "Deleted";
  const check: never = action;
  return check;
}
```

```typescript
/** Example 3: debugNever helper */
function debugNever(value: never, context: string): never {
  console.error(`Unhandled case in ${context}:`, value);
  throw new Error(`Unhandled: ${JSON.stringify(value)}`);
}

function process(action: Action): string {
  if (action === "create") return "Created";
  return debugNever(action, "process");
}
```
