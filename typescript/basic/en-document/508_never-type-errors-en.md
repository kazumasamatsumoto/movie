# #508 "Never-Type Errors"

Shikoku Metan: "The never type can turn missing branches into compile errors."
Zundamon: "In handleAction() forgetting delete made const check: never = action; explode."
Shikoku Metan: "Adding an archive action produced the same compile-time warning."
Zundamon: "When handle() only returns for create, the rest collapses to never."
Shikoku Metan: "Guarding early lets us notice omissions later."
Zundamon: "The final example handles create/update/delete and the check passes."
Shikoku Metan: "Only a truly exhaustive branch allows assigning to never."
Zundamon: "Let never errors keep union omissions at zero."

---

## 📺 Code for Display

```typescript
/** Example 1: Missing delete */
type Action = "create" | "update" | "delete";

function handleAction(action: Action) {
  if (action === "create") return "Created";
  if (action === "update") return "Updated";
  const check: never = action; // compile-time error when delete is missing
}

/** Example 2: Added cases */
type ExtendedAction = "create" | "update" | "delete" | "archive";

function handle(action: ExtendedAction) {
  if (action === "create") return "Created";
  const check: never = action; // archive is unhandled
}

/** Example 3: Fully exhaustive */
function handleAll(action: Action) {
  if (action === "create") return "Created";
  if (action === "update") return "Updated";
  if (action === "delete") return "Deleted";
  const check: never = action; // unreachable when all cases are covered
  return check;
}
```
