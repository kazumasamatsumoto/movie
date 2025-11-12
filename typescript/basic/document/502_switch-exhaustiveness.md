# #502 「switch文の網羅性」

四国めたん「次はswitch文で網羅性を確かめよう。」
ずんだもん「handleAction()はcreate/update/deleteを全部回してたね。」
四国めたん「defaultでconst exhaustive: never = action; を置けば安心。」
ずんだもん「共通のassertNever()を作って再利用できるのが便利。」
四国めたん「process()みたいに複数のswitchでも同じ関数を呼べる。」
ずんだもん「Status型でsuccessを書き忘れたらassertNever(status)が怒るの。」
四国めたん「Unionを増やした瞬間に未処理が発覚するね。」
ずんだもん「switchを書くときはdefaultを監視役にしよう。」

---

## 📺 画面表示用コード

```typescript
/** Example 1: Actionの網羅性 */
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
      throw new Error(`未処理: ${exhaustive}`);
  }
}

/** Example 2: assertNeverの再利用 */
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

/** Example 3: Statusのチェック */
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
