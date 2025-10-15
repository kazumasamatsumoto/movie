# #1107 「型推論」

四国めたん「concatやslice、flat系でも型推論が働きます。」
ずんだん「mapと同様に戻り値の配列型が自動で決まるんだね。」
四国めたん「はい、flatMapはコールバックの戻り値から推論されます。」
ずんだん「推論結果が期待と違う場合だけ型注釈を補おう。」
四国めたん「型推論を活かしてコードを簡潔にしてください。」
ずんだん「TypeScriptの強みを活かそう！」

---

## 📺 画面表示用コード

```typescript
const numbers = [1, 2, 3];

const moreNumbers = numbers.concat(4); // number[]
const sub = numbers.slice(0, 2); // number[]
const flattened = [[1], [2]].flat(); // number[]
const mapped = numbers.flatMap((value) => [value, value * 2]); // number[]
```
