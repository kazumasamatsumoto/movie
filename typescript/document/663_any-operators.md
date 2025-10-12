# #663 「anyで演算子を使う危険」

四国めたん「anyに演算子を使うと予期しない結果になります」
ずんだもん「文字列とオブジェクトの足し算で[object Object]になるみたいなパターンだね」
四国めたん「はい。比較演算でも常にfalseになったりしてバグにつながります」
ずんだもん「unknownで型を確定させてから演算すれば安全だよ」
四国めたん「演算が必要なら型を厳密に管理しましょう」
ずんだもん「算術ロジックにanyを入れないことが鉄則だね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: anyで演算 */
const a: any = { price: 100 };
const total = a + 200; // "[object Object]200"

/** Example 2: 比較の罠 */
const result = a > 0; // falseになる場合がある

/** Example 3: 型チェック */
function ensureNumber(value: unknown): number {
  if (typeof value !== "number") throw new TypeError("number required");
  return value;
}
```
