# #520 「網羅性まとめ」

四国めたん「never回の締めに網羅性の総まとめをしよう。」
ずんだもん「Statusのhandle()はpending/success/errorをifで全部返してたね。」
四国めたん「return exhaustiveCheck(status); を置いておけば追加時に失敗する。」
ずんだもん「Result型のprocess()もokフラグでvalueかerrorを選んでたのだ。」
四国めたん「EventHandlerはswitchでclickとkeypressを処理してdefaultでexhaustiveCheck(event)。」
ずんだもん「この3パターンを覚えれば大体のUnionに応用できるよ。」
四国めたん「never型を味方につけて仕様変更にも強くなろう。」
ずんだもん「今日から網羅性チェックの伝道師なのだ。」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 基本形 */
type Status = "pending" | "success" | "error";

function exhaustiveCheck(value: never): never {
  throw new Error(`Unhandled: ${value}`);
}

function handle(status: Status): string {
  if (status === "pending") return "処理中";
  if (status === "success") return "成功";
  if (status === "error") return "エラー";
  return exhaustiveCheck(status);
}

/** Example 2: Result型 */
type Result<T, E> =
  | { ok: true; value: T }
  | { ok: false; error: E };

function process<T, E>(result: Result<T, E>): T {
  if (result.ok) return result.value;
  if (!result.ok) throw result.error;
  return exhaustiveCheck(result);
}

/** Example 3: イベント処理 */
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
