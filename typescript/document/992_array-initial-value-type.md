# #992 「初期値型」

四国めたん「reduceの初期値型はアキュムレータ型そのものです。」
ずんだもん「初期値にオブジェクトを入れればアキュムレータもオブジェクトになるんだね。」
四国めたん「初期値を省略すると配列要素から推論されるため意図を満たさないことがあります。」
ずんだもん「初期値は明示的に指定するのが安全だよ。」
四国めたん「初期値型を理解してreduceを使いこなしてください。」
ずんだもん「意図しない推論を避けよう！」

---

## 📺 画面表示用コード

```typescript
const values = [1, 2, 3];

/** Example 1: 初期値明示 */
const product = values.reduce((acc, cur) => acc * cur, 1); // acc: number

/** Example 2: オブジェクト初期値 */
const summary = values.reduce(
  (acc, cur) => ({ sum: acc.sum + cur, max: Math.max(acc.max, cur) }),
  { sum: 0, max: Number.NEGATIVE_INFINITY }
);

/** Example 3: 省略時 */
const withoutInit = values.reduce((acc, cur) => acc + cur); // 最初の要素が初期値
```
