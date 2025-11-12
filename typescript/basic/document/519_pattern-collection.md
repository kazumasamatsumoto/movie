# #519 「パターン集」

四国めたん「網羅性チェックの代表パターンを見ていこう。」
ずんだもん「まずはReducerパターンでCounterActionをswitchしてたね。」
四国めたん「default: return exhaustiveCheck(action); で新アクションを検知できる。」
ずんだもん「Commandパターンではkindを見てsave/load/deleteの関数を呼んでたのだ。」
四国めたん「Stateパターンはstatusで表示ラベルを切り替えていたよ。」
ずんだもん「exhaustiveCheck(state)が接続状態の抜け漏れを防いでくれる。」
四国めたん「パターンを覚えておけば他のドメインにも転用しやすい。」
ずんだもん「Unionを設計するときのテンプレとして役立つね。」

---

## 📺 画面表示用コード

```typescript
/** Example 1: Reducerパターン */
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

/** Example 2: Commandパターン */
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

/** Example 3: Stateパターン */
type ConnectionState =
  | { status: "disconnected" }
  | { status: "connecting"; attempt: number }
  | { status: "connected"; sessionId: string };

function getLabel(state: ConnectionState): string {
  switch (state.status) {
    case "disconnected":
      return "切断";
    case "connecting":
      return `接続中(${state.attempt})`;
    case "connected":
      return `接続済(${state.sessionId})`;
    default:
      return exhaustiveCheck(state);
  }
}
```
