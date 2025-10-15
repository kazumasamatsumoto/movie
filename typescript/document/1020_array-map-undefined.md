# #1020 「undefinedは消えない」

四国めたん「mapはundefinedを返しても要素が消えるわけではありません。」
ずんだもん「mapは常に元の長さと同じ配列を返すんだね。」
四国めたん「はい、空要素を除去したいときはfilterを使いましょう。」
ずんだもん「mapでundefinedを返すとundefinedが含まれる配列になるよ。」
四国めたん「挙動を理解して使い分けてください。」
ずんだもん「意図しないundefinedに注意してね！」

---

## 📺 画面表示用コード

```typescript
const values = ["ok", "", "ng"];

/** Example 1: mapでundefined */
const maybe = values.map((value) => (value ? value : undefined));
// 型: (string | undefined)[]

/** Example 2: filterで除去 */
const filtered = maybe.filter((value): value is string => value !== undefined);

/** Example 3: flatMapで除去 */
const compact = values.flatMap((value) => (value ? [value] : []));
```
