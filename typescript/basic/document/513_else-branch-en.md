# #513 "Else Branches"

Shikoku Metan: "Else branches can host exhaustiveness hints."
Zundamon: "getLabel() returned every State via if-else."
Shikoku Metan: "Dropping const check: never = state; inside the final else exposes gaps."
Zundamon: "Extending State with timeout instantly triggered a compile error."
Shikoku Metan: "A sloppy else that swallows everything is dangerous."
Zundamon: "We also reviewed the correct switch-based implementation."
Shikoku Metan: "Explicit branches beat vague fall-through paths."
Zundamon: "Pair them with never checks to keep label helpers safe."

---

## 📺 Code for Display

```typescript
/** Example 1: Exhaustive if-else */
type State = "idle" | "loading" | "success" | "error";

function getLabel(state: State): string {
  if (state === "idle") return "Idle";
  else if (state === "loading") return "Loading";
  else if (state === "success") return "Done";
  else if (state === "error") return "Error";
  else {
    const check: never = state;
    return check;
  }
}

/** Example 2: New case causes errors */
type ExtendedState = State | "timeout";

function brokenLabel(state: ExtendedState): string {
  if (state === "idle") return "Idle";
  else {
    const check: never = state; // timeout hits here
    return "";
  }
}

/** Example 3: Safe switch */
function safeLabel(state: ExtendedState): string {
  switch (state) {
    case "idle":
      return "Idle";
    case "loading":
      return "Loading";
    case "success":
      return "Done";
    case "error":
      return "Error";
    case "timeout":
      return "Timeout";
  }
}
```
