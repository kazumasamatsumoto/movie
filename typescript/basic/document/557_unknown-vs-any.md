# #557 「unknownとanyの違い」

四国めたん「unknownとanyは受け取れる値は同じですが挙動が異なります」
ずんだもん「anyは全部許される代わりに実行時までエラーがわからないんだよね」
四国めたん「unknownは操作前に型チェックを要求し、誤用を止めます」
ずんだもん「なるほど、安全性を優先したいならunknownを使えばいいのか」
四国めたん「はい。意図的に型安全性を下げたいとき以外はunknown推奨です」
ずんだもん「コードレビューでもunknownを基準に考えよう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: anyでの落とし穴 */
const anyValue: any = JSON.parse("null");
anyValue.trim(); // runtime TypeError

/** Example 2: unknownでの安全 */
const unknownValue: unknown = JSON.parse("null");
// unknownValue.trim(); // ❌ コンパイルエラー
if (typeof unknownValue === "string") {
  unknownValue.trim();
}

/** Example 3: 関数シグネチャ差 */
function handleAny(value: any) {
  value.toFixed();
}
function handleUnknown(value: unknown) {
  if (typeof value === "number") value.toFixed();
}
```
