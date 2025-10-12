# #658 「anyが招くランタイムエラー③」

四国めたん「3つ目はanyで数値演算をしてNaNや例外が発生するケースです」
ずんだもん「value * 2 を呼んだら value がオブジェクトだったパターンだね」
四国めたん「はい。静的チェックが効かないので計算結果が壊れます」
ずんだもん「typeofやNumber.isFiniteで検証すると安心だよ」
四国めたん「演算前に型を確定させることが重要です」
ずんだもん「計算ロジックにanyを持ち込まないようにしよう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: anyで演算 */
const value: any = { price: 100 };
const total = value * 2; // NaN

/** Example 2: unknownで型チェック */
const safeValue: unknown = { price: 100 };
if (typeof safeValue === "number") {
  console.log(safeValue * 2);
}

/** Example 3: 検証ユーティリティ */
const toNumber = (input: unknown): number => {
  if (typeof input === "number" && Number.isFinite(input)) return input;
  throw new TypeError("number required");
};
```
