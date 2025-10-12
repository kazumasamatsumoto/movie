# #551 「unknown型の安全な扱い」

四国めたん「TypeScript v5.9のunknown型について学びましょう！」
ずんだもん「型安全なanyって聞くけど、どんな場面で使うの？」
四国めたん「unknownはトップ型なので何でも代入できますが、anyと違って直接プロパティに触れるとエラーになります。」
ずんだもん「じゃあ演算もメソッド呼び出しもできないんだね？」
四国めたん「はい。typeofやinstanceof、in演算子で型ガードしてから扱います。」
ずんだもん「Array.isArrayやカスタム型ガードで段階的に絞り込むのが安全だよね。」
四国めたん「必要ならasで型アサーションも使えますが、チェックとセットで行うのがベストプラクティスです。」
ずんだもん「APIレスポンスやtry-catchのerrorをunknownで受けて型安全に処理しよう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 宣言と制約 */
declare const input: string; // 外部入力
let payload: unknown = JSON.parse(input);
payload; // ✅ 参照は可能
// payload.id;          // ❌ プロパティアクセスはエラー
// payload();           // ❌ 関数呼び出しはエラー
// payload + 1;         // ❌ 演算もエラー

/** Example 2: typeof / instanceof ガード */
if (typeof payload === "string") {
  const upper = payload.toUpperCase();
} else if (payload instanceof Error) {
  console.error(payload.message);
} else {
  console.log("unknown payload", payload);
}

/** Example 3: カスタム型ガード */
type User = { id: number; name: string };
function isUser(value: unknown): value is User {
  return typeof value === "object"
    && value !== null
    && "id" in value
    && typeof (value as Record<string, unknown>).id === "number";
}
if (isUser(payload)) {
  console.log(payload.id);
}
```
