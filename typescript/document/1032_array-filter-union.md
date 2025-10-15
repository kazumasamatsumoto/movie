# #1032 「Union型配列のfilter」

四国めたん「Union型配列ではfilterが特に力を発揮します。」
ずんだもん「型述語を使えばstringだけ、numberだけに絞れるんだね。」
四国めたん「はい、Union要素を安全に扱うための定番テクニックです。」
ずんだもん「まずは(string | number)[]をfilterしてみよう。」
四国めたん「Union型配列のfilterパターンを覚えてください。」
ずんだもん「複雑なデータも扱いやすくなるよ！」

---

## 📺 画面表示用コード

```typescript
const mixed: (string | number | boolean)[] = ["ok", 200, true, "ng"];

const isString = (value: string | number | boolean): value is string => typeof value === "string";
const isNumber = (value: string | number | boolean): value is number => typeof value === "number";

/** Example 1: stringだけ */
const strings = mixed.filter(isString);

/** Example 2: numberだけ */
const numbers = mixed.filter(isNumber);

/** Example 3: 両方 */
const stringOrNumber = mixed.filter((value): value is string | number => typeof value !== "boolean");
```
