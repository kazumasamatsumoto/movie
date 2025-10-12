# #561 「unknownと型推論」

四国めたん「unknownが入ると型推論は安全側へ振れます」
ずんだもん「Unionの一部がunknownだと結果もunknown寄りになるんだよね」
四国めたん「はい。ジェネリクスでも束縛が緩むので手動で絞る必要があります」
ずんだもん「推論結果を意識して型ガードを用意しておくのが大事だよ」
四国めたん「推論結果がanyにならない点もポイントです」
ずんだもん「unknownを通して安全な推論チェーンを作ろう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 推論結果 */
const mix = Math.random() > 0.5 ? "str" : 10;
const inferred: unknown = mix;

/** Example 2: 条件付き型での推論 */
type Infer<T> = T extends { value: infer U } ? U : unknown;
type Result = Infer<{ value: number }>; // number

/** Example 3: ジェネリック関数内の推論 */
function pick<T>(value: T): T extends string ? string : unknown {
  return value as any;
}
```
