# #1030 「型述語 - (value: T) => value is U」

四国めたん「filterには型述語シグネチャも用意されています。」
ずんだもん「(value: T) => value is U を返すと結果がU[]になるんだね。」
四国めたん「Union型の配列から特定の型だけ取り出すときに便利です。」
ずんだもん「型述語を覚えるとfilterの活用範囲が広がるよ。」
四国めたん「具体的な使い方を次で見ていきましょう。」
ずんだもん「まずはシグネチャを覚えてね！」

---

## 📺 画面表示用コード

```typescript
const values: (string | number)[] = ["ok", 200, "ng"];

const isString = (value: string | number): value is string => typeof value === "string";

/** Example 1: 型述語シグネチャ */
const strings = values.filter(isString); // string[]

/** Example 2: インライン */
const numbers = values.filter((value): value is number => typeof value === "number");

/** Example 3: 再利用 */
function onlyStrings<T>(values: (T | string)[]): string[] {
  return values.filter((value): value is string => typeof value === "string");
}
```
