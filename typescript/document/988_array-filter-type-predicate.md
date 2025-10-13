# #988 「filter()の型述語」

四国めたん「filterに型述語を渡すと結果の配列型を狭くできます。」
ずんだもん「(item): item is string => typeof item === "string" みたいなコールバックだね。」
四国めたん「はい、配列操作の定番テクニックです。」
ずんだもん「型述語を共通化すると複数箇所で再利用できるよ。」
四国めたん「filterの型述語を積極的に活用しましょう。」
ずんだもん「Union配列を扱いやすくなるよ！」

---

## 📺 画面表示用コード

```typescript
const tokens: (string | number)[] = ["ok", 200, "ng"];

/** Example 1: 述語関数 */
const isString = (value: string | number): value is string => typeof value === "string";

/** Example 2: filter */
const stringTokens = tokens.filter(isString); // string[]

/** Example 3: numbers */
const numberTokens = tokens.filter((value): value is number => typeof value === "number");
```
