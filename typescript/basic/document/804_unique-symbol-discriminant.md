# #804 「判別プロパティ」

四国めたん「判別ユニオンでunique symbolを使うと衝突しないタグが作れます。」
ずんだもん「stringリテラルよりも外部入力と混ざらないから安心だね。」
四国めたん「typeofタグで安全に型を絞り込めます。」
ずんだもん「switch文にもそのまま使えるよ。」
四国めたん「unique symbolなら判別値が他のUnionと重ならないことが保証されます。」
ずんだもん「タグ型を整えてエラーのない分岐を書こう！」
四国めたん「型レベルで判別プロパティを設計してみてください。」
ずんだもん「unique symbolで強固なユニオンを作ろう！」

---

## 📺 画面表示用コード

```typescript
const CREATE = Symbol("create");
const UPDATE = Symbol("update");

/** 判別ユニオン */
type Command =
  | { kind: typeof CREATE; payload: { name: string } }
  | { kind: typeof UPDATE; payload: { id: number; name: string } };

function handleCommand(command: Command) {
  switch (command.kind) {
    case CREATE:
      return `create ${command.payload.name}`;
    case UPDATE:
      return `update ${command.payload.id}`;
  }
}
```
