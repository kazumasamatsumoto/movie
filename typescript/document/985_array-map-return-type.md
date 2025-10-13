# #985 「map()の戻り値型」

四国めたん「mapは常に新しい配列を返し、要素型はコールバックの戻り値型です。」
ずんだもん「number[]にmapしてbooleanを返すとboolean[]になるんだね。」
四国めたん「はい、型推論が働くので戻り値型を意識して設計しましょう。」
ずんだもん「Promiseを返すとPromiseの配列になるだけでawaitはされない点にも注意だよ。」
四国めたん「mapの戻り値型を理解してチェーンを安全に書きましょう。」
ずんだもん「結果配列の型を意識してね！」

---

## 📺 画面表示用コード

```typescript
const numbers = [1, 2, 3];

/** Example 1: boolean[] */
const flags = numbers.map((n) => n > 1); // boolean[]

/** Example 2: Promise */
const requests = numbers.map((n) => fetch(`/api/${n}`)); // Promise<Response>[]

/** Example 3: map + map */
const lengths = numbers
  .map((n) => n.toString()) // string[]
  .map((s) => s.length); // number[]
```
