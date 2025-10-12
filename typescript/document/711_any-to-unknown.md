# #711 「unknown型への置き換え」

四国めたん「anyの代替として最も簡単なのがunknownです」
ずんだもん「ガードを強制して安全性を取り戻せるんだよね」
四国めたん「はい。まずunknownに変えてから必要な型ガードやアサーションを追加します」
ずんだもん「コンパイルエラーが誘導してくれるから段階移行にぴったりだよ」
四国めたん「unknownは万能な受け皿でありながら静的保証を保てます」
ずんだもん「anyを見つけたら真っ先にunknown化しよう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: any → unknown */
let payload: unknown = JSON.parse("{}");
// payload.user; // ❌ guardが必要

/** Example 2: 型ガード */
const hasUser = (value: unknown): value is { user: { name: string } } =>
  typeof value === "object" && value !== null && "user" in value;

/** Example 3: 利用 */
if (hasUser(payload)) console.log(payload.user.name);
```
