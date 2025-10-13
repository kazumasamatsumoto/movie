# #921 「[1, 2, 3]の型」

四国めたん「具体的に[1, 2, 3]の型はnumber[]に推論されます。」
ずんだもん「要素が全部numberだからだね。」
四国めたん「はい、constで宣言すると配列自体は再代入不可ですが型はnumber[]のままです。」
ずんだもん「as constを使うとreadonly [1, 2, 3]になるよ。」
四国めたん「Mutableな配列として扱いたいならそのまま推論させるか型注釈を付けましょう。」
ずんだもん「推論結果を理解して使い分けてね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 推論 */
const numbers = [1, 2, 3]; // number[]

/** Example 2: const */
const readonlyNumbers = [1, 2, 3] as const; // readonly [1, 2, 3]

/** Example 3: 型注釈 */
const typed: number[] = [1, 2, 3];
```
