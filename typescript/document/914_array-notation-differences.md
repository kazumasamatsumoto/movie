# #914 「記法の違い」

四国めたん「Array<T>とT[]は意味が同じですが、書き心地が違います。」
ずんだもん「ジェネリクスと組み合わせると読みやすい方が変わるんだね。」
四国めたん「型パラメータを扱うときはArray<T>が明示的で、単純な型ではT[]が短いです。」
ずんだもん「JSX内ではT[]が安全って聞いたことあるよ。」
四国めたん「正確にはArray<T>がJSXタグと衝突しにくいという利点です。」
ずんだもん「違いを理解して状況に応じて選ぼう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: ジェネリクスとの相性 */
function wrap<T>(items: Array<T>): Array<T> {
  return [...items];
}

/** Example 2: シンプル型 */
const flags: boolean[] = [true, false];

/** Example 3: JSX内での利用 */
// const nodes = <T[]>(...); // JSXタグに見えてしまう
const saferNodes: Array<ReactNode> = [];
```
