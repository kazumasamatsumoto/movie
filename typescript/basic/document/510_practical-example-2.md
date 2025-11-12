# #510 「実践例(2)」

四国めたん「実践例その2はイベント駆動アプリだよ。」
ずんだもん「DomainEventにはUserCreated/Updated/Deletedがあったね。」
四国めたん「EventHandler.handle()はif-elseで分岐してexhaustiveCheck(event)で締めてた。」
ずんだもん「メソッドを分けても最後にneverチェックを忘れなかったのだ。」
四国めたん「APIレスポンスのUnionもstatusでsuccess/errorを切り替えてた。」
ずんだもん「process()でsuccessならdataを返し、errorならthrowしてたね。」
四国めたん「const check: never = res; を置けば新しいstatus追加にすぐ気付ける。」
ずんだもん「実務的なUnionもneverで守って信頼性アップだ。」

---

## 📺 画面表示用コード

```typescript
/** Example 1: ドメインイベント */
type DomainEvent =
  | { type: "UserCreated"; userId: string }
  | { type: "UserUpdated"; userId: string; data: unknown }
  | { type: "UserDeleted"; userId: string };

/** Example 2: EventHandlerクラス */
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

/** Example 3: APIレスポンス */
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
