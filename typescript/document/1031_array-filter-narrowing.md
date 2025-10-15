# #1031 「型の絞り込み」

四国めたん「型述語を使うとfilterの結果で型が絞り込まれます。」
ずんだもん「filter後の配列をそのまま扱えるから便利だね。」
四国めたん「はい、後段の処理でキャストが不要になります。」
ずんだもん「型安全性が高まるから積極的に活用しよう。」
四国めたん「絞り込みの効果を確認してみましょう。」
ずんだもん「Union配列を扱いやすくなるよ！」

---

## 📺 画面表示用コード

```typescript
const payload: (string | number)[] = ["start", 200, 404, "end"];

const isNumber = (value: string | number): value is number => typeof value === "number";

/** Example 1: filterで絞り込み */
const numbers = payload.filter(isNumber);

/** Example 2: 後段処理 */
const total = numbers.reduce((acc, cur) => acc + cur, 0);

/** Example 3: string版 */
const strings = payload.filter((value): value is string => typeof value === "string");
```
