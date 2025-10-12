# #559 「unknownは型階層のトップ型」

四国めたん「unknownはTypeScriptの型階層でトップ型に位置します」
ずんだもん「つまり全ての型がunknownに代入できるってことだね」
四国めたん「はい。逆にunknownから他の型に代入するには型チェックが必要です」
ずんだもん「neverがボトム型で、unknownがトップ型って覚えると整理しやすいよ」
四国めたん「型理論のサブタイプ関係そのものですね」
ずんだもん「理論を知るとジェネリクスの設計にも活きるよ！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 代入は常に可能 */
let topType: unknown;
topType = 1;
topType = "string";
topType = Symbol("id");

/** Example 2: neverからunknownへ */
function absurd(value: never): unknown {
  return value;
}

/** Example 3: 条件付き型でのトップ型 */
type Flatten<T> = T extends unknown ? T : never;
type Result = Flatten<string | number>; // string | number
```
