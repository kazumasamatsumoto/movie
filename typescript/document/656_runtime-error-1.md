# #656 「anyが招くランタイムエラー①」

四国めたん「anyによる典型的なランタイムエラーは存在しないプロパティ参照です」
ずんだもん「payload.user.nameって書いて、実際はuserが無かったパターンだね」
四国めたん「はい。コンパイルが止めないので本番で落ちる危険があります」
ずんだもん「unknownならガードが必須になるから防げるよ」
四国めたん「プロパティアクセスこそanyのリスクが顕在化する場面です」
ずんだもん「早めにunknownに置き換えよう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: anyで落ちる */
const payload: any = {};
console.log(payload.user.name); // TypeError

/** Example 2: unknownで防ぐ */
const safePayload: unknown = {};
if (typeof safePayload === "object" && safePayload !== null && "user" in safePayload) {
  console.log((safePayload as { user: { name: string } }).user.name);
}

/** Example 3: ガード関数 */
const hasUser = (value: unknown): value is { user: { name: string } } =>
  typeof value === "object" && value !== null && "user" in value;
```
