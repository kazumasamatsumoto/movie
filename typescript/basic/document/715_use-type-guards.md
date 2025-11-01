# #715 「型ガードの活用」

四国めたん「anyをunknownに変えた後は型ガードで安全に扱いましょう」
ずんだもん「ユーザー定義型ガードなら再利用しやすいんだよね」
四国めたん「はい。型述語を返す関数を作ると補完とチェックが両立します」
ずんだもん「複数のガードを組み合わせてネスト構造も守りたいよ」
四国めたん「ガードを整備すればanyに戻らない開発ができます」
ずんだもん「ガードライブラリをプロジェクト資産にしよう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 型ガード */
function isUser(value: unknown): value is { id: number; name: string } {
  return typeof value === "object"
    && value !== null
    && "id" in value
    && typeof (value as Record<string, unknown>).id === "number"
    && typeof (value as Record<string, unknown>).name === "string";
}

/** Example 2: ネスト対応ガード */
const hasProfile = (value: unknown): value is { profile: { age: number } } =>
  typeof value === "object"
  && value !== null
  && "profile" in value
  && typeof (value as Record<string, unknown>).profile === "object";

/** Example 3: 利用 */
const payload: unknown = JSON.parse("{}");
if (isUser(payload)) console.log(payload.name);
```
