# #943 「rest要素」

四国めたん「分割代入のrest要素を使うと残りの配列をまとめて取得できます。」
ずんだもん「const [head, ...rest] = list; みたいな書き方だね。」
四国めたん「はい、rest部分の型は元の配列と同じ要素型になります。」
ずんだもん「タプルのrestではより細かい型が推論されるよ。」
四国めたん「rest要素を活用して配列操作をシンプルにしましょう。」
ずんだもん「便利な構文だから覚えておこう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 基本 */
const queue = ["a", "b", "c"];
const [first, ...others] = queue; // others: string[]

/** Example 2: タプルrest */
const tuple: [string, ...number[]] = ["head", 1, 2];
const [label, ...numbers] = tuple; // numbers: number[]

/** Example 3: 関数 */
function tail<T>([_, ...rest]: T[]): T[] {
  return rest;
}
```
