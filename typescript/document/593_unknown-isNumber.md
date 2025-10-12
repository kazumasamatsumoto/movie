# #593 「isNumber型ガード」

四国めたん「isNumber関数でunknownを数値に絞り込みましょう」
ずんだもん「戻り値をx is numberにすれば再利用できるね」
四国めたん「はい。NaN排除ロジックと組み合わせると堅牢です」
ずんだもん「フィルタやreduceにもそのまま渡せるよ」
四国めたん「数値ドメインの安全性を高める基礎テクです」
ずんだもん「データ処理がスムーズになるね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: isNumber定義 */
function isNumber(value: unknown): value is number {
  return typeof value === "number" && !Number.isNaN(value);
}

/** Example 2: 配列フィルタ */
const list: unknown[] = [1, "2", 3];
const numbers = list.filter(isNumber);

/** Example 3: sum処理 */
const sum = numbers.reduce((acc, current) => acc + current, 0);
```
