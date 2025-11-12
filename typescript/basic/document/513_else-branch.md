# #513 「else節」

四国めたん「else節にも網羅性のヒントを仕込めるよ。」
ずんだもん「StateのgetLabel()はif-elseで全状態を返してたね。」
四国めたん「最後のelseでconst check: never = state; と書けば漏れを検出できる。」
ずんだもん「Stateにtimeoutを足した例では即座に型エラーになってたのだ。」
四国めたん「雑にelseだけ書くと全部がそこに落ちて危険って話。」
ずんだもん「ちゃんとswitchで全ケースを書く正しい実装も確認したよ。」
四国めたん「意味のないelse節を使うより明示的な分岐が安心。」
ずんだもん「neverチェックを添えて安全なラベル関数を育てよう。」

---

## 📺 画面表示用コード

```typescript
/** Example 1: if-elseで網羅 */
type State = "idle" | "loading" | "success" | "error";

function getLabel(state: State): string {
  if (state === "idle") return "待機中";
  else if (state === "loading") return "読込中";
  else if (state === "success") return "成功";
  else if (state === "error") return "エラー";
  else {
    const check: never = state;
    return check;
  }
}

/** Example 2: 追加ケースでエラー */
type ExtendedState = State | "timeout";

function brokenLabel(state: ExtendedState): string {
  if (state === "idle") return "待機中";
  else {
    const check: never = state; // timeoutで型エラー
    return "";
  }
}

/** Example 3: switchで正しく処理 */
function safeLabel(state: ExtendedState): string {
  switch (state) {
    case "idle":
      return "待機中";
    case "loading":
      return "読込中";
    case "success":
      return "成功";
    case "error":
      return "エラー";
    case "timeout":
      return "タイムアウト";
  }
}
```
