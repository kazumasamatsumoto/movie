# #591 「カスタム型ガード関数」

四国めたん「カスタム型ガード関数を作ればunknownを再利用可能に絞れます」
ずんだもん「value is Userみたいな型述語を返すやつだね」
四国めたん「はい。複数のチェックをまとめてチームで共有できます」
ずんだもん「ドメインごとのガードを用意するとテストもしやすいよ」
四国めたん「再利用性が高くなるほどunknown活用が楽になります」
ずんだもん「型ガード関数をプロジェクトの資産にしよう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: ユーザーガード */
type User = { id: number; name: string };
const isUser = (value: unknown): value is User =>
  typeof value === "object"
  && value !== null
  && "id" in value
  && typeof (value as Record<string, unknown>).id === "number"
  && typeof (value as Record<string, unknown>).name === "string";

/** Example 2: 設定ガード */
type Config = { debug?: boolean };
const isConfig = (value: unknown): value is Config =>
  typeof value === "object" && value !== null;

/** Example 3: 利用例 */
const payload: unknown = { id: 1, name: "Mochi" };
if (isUser(payload)) console.log(payload.name);
```
