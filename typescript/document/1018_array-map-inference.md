# #1018 「型推論」

四国めたん「mapはコールバックの戻り値型を自動推論します。」
ずんだもん「型注釈なしでもstring[]やnumber[]に推論されるんだね。」
四国めたん「はい、複雑なUnionやオブジェクトでも推論が働きます。」
ずんだもん「推論結果が期待と違うときだけ型注釈を追加しよう。」
四国めたん「型推論を信頼しつつ、必要に応じて補助を入れてください。」
ずんだもん「開発効率が上がるよ！」

---

## 📺 画面表示用コード

```typescript
const numbers = [1, 2, 3];
const inferredStrings = numbers.map((value) => value.toString());

type Inferred = typeof inferredStrings; // string[]

/** Example 1: オブジェクト */
const objects = numbers.map((value) => ({ value, even: value % 2 === 0 }));

/** Example 2: Union */
const union = numbers.map((value) => (value % 2 ? value : value.toString()));

type UnionResult = typeof union; // (string | number)[]

/** Example 3: 補助 */
const forced = numbers.map<number>((value) => Number(value));
```
