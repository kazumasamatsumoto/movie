# #583 「typeof x === "number"」

四国めたん「typeof x === "number"でunknownを数値に絞り込みます」
ずんだもん「数値演算や比較がすぐに使えるようになるね」
四国めたん「NaNチェックも組み合わせるとより安全です」
ずんだもん「整数だけ許したいときはNumber.isIntegerも使えるよ」
四国めたん「検証を通した上で演算を行う癖をつけましょう」
ずんだもん「数値ガードでシビアなロジックを守ろう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: numberガード */
function increment(value: unknown) {
  if (typeof value === "number") {
    return value + 1;
  }
  return null;
}

/** Example 2: NaN排除 */
function isFiniteNumber(value: unknown): value is number {
  return typeof value === "number" && Number.isFinite(value);
}

/** Example 3: フィルタリング */
const mixed: unknown[] = [1, "2", 3];
const numbers = mixed.filter((item): item is number => typeof item === "number");
```
