# #548 「デバッグ」

四国めたん「never周りの型エラーは段階的にデバッグしよう。」
ずんだもん「手順1では型エラーのメッセージを確認するんだったね。」
四国めたん「Action = 'create' | 'update' | 'delete'でcreateしか書かないと`\"update\" | \"delete\"`が残る。」
ずんだもん「step2ではVSCodeでactionをホバーして残りのUnionを調べてた。」
四国めたん「update/deleteを処理した後にconst check: never = action; を置けば解決。」
ずんだもん「step3ではdebugNever()ヘルパーでランタイムに情報を出してたよ。」
四国めたん「Unhandled case in process: 'update' みたいなログが出せるのが便利。」
ずんだもん「焦らずエラー→残り確認→ヘルパー活用の順で直そう。」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 型エラーを確認 */
type Action = "create" | "update" | "delete";

function handle(action: Action): string {
  if (action === "create") return "Created";
  const check: never = action;
  return "";
}
```

```typescript
/** Example 2: 残りを処理 */
function handleFixed(action: Action): string {
  if (action === "create") return "Created";
  if (action === "update") return "Updated";
  if (action === "delete") return "Deleted";
  const check: never = action;
  return check;
}
```

```typescript
/** Example 3: debugNeverヘルパー */
function debugNever(value: never, context: string): never {
  console.error(`Unhandled case in ${context}:`, value);
  throw new Error(`Unhandled: ${JSON.stringify(value)}`);
}

function process(action: Action): string {
  if (action === "create") return "Created";
  return debugNever(action, "process");
}
```
