# #508 「never型での型エラー」

四国めたん「never型は実装漏れを型エラーにしてくれるよ。」
ずんだもん「handleAction()はdeleteを書き忘れるとconst check: never = action;で怒られた。」
四国めたん「Actionにarchiveを追加した例でも同じくエラーが出てたね。」
ずんだもん「handle()でcreateしか返さないと残りが全部never扱いになるのだ。」
四国めたん「開発初期にガードを入れておくと後で気付ける。」
ずんだもん「最後の例ではcreate/update/deleteを全部処理してからcheck: never = action;が通ってた。」
四国めたん「つまり完全に網羅しているときだけnever代入が成功する。」
ずんだもん「never型エラーを友達にしてUnion漏れをゼロにしよう。」

---

## 📺 画面表示用コード

```typescript
/** Example 1: deleteを忘れたケース */
type Action = "create" | "update" | "delete";

function handleAction(action: Action) {
  if (action === "create") return "Created";
  if (action === "update") return "Updated";
  const check: never = action; // deleteを忘れるとここで型エラー
}

/** Example 2: ケース追加でエラー */
type ExtendedAction = "create" | "update" | "delete" | "archive";

function handle(action: ExtendedAction) {
  if (action === "create") return "Created";
  const check: never = action; // archiveなどが未処理
}

/** Example 3: 網羅している場合 */
function handleAll(action: Action) {
  if (action === "create") return "Created";
  if (action === "update") return "Updated";
  if (action === "delete") return "Deleted";
  const check: never = action; // ここには到達しない
  return check;
}
```
