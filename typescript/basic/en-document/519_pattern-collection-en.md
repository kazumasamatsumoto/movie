# #519 "Pattern Catalog"

Shikoku Metan: "Let's tour common exhaustiveness patterns."
Zundamon: "The reducer pattern switched over CounterAction."
Shikoku Metan: "default: return exhaustiveCheck(action); flags new actions."
Zundamon: "The command pattern branched on kind to call save/load/delete."
Shikoku Metan: "The state pattern mapped status to display labels."
Zundamon: "exhaustiveCheck(state) guards connection states against drift."
Shikoku Metan: "Memorize these patterns to reuse them elsewhere."
Zundamon: "They're practical templates for union design."

---

## 📺 Code for Display

```typescript
/** Example 1: Reducer pattern */
type CounterAction =
  | { type: "increment"; by: number }
  | { type: "decrement"; by: number }
  | { type: "reset" };

function counterReducer(state: number, action: CounterAction): number {
  switch (action.type) {
    case "increment":
      return state + action.by;
    case "decrement":
      return state - action.by;
    case "reset":
      return 0;
    default:
      return exhaustiveCheck(action);
  }
}

/** Example 2: Command pattern */
type AppCommand =
  | { kind: "save"; data: string }
  | { kind: "load"; id: number }
  | { kind: "delete"; id: number };

function executeCommand(cmd: AppCommand): void {
  if (cmd.kind === "save") save(cmd.data);
  else if (cmd.kind === "load") load(cmd.id);
  else if (cmd.kind === "delete") remove(cmd.id);
  else exhaustiveCheck(cmd);
}

/** Example 3: State pattern */
type ConnectionState =
  | { status: "disconnected" }
  | { status: "connecting"; attempt: number }
  | { status: "connected"; sessionId: string };

function getLabel(state: ConnectionState): string {
  switch (state.status) {
    case "disconnected":
      return "Disconnected";
    case "connecting":
      return `Connecting (${state.attempt})`;
    case "connected":
      return `Connected (${state.sessionId})`;
    default:
      return exhaustiveCheck(state);
  }
}
```
