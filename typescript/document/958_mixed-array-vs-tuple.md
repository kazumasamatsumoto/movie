# #958 「Union配列 vs タプル」

四国めたん「混合型配列とタプルの違いを整理しましょう。」
ずんだもん「Union配列は要素数が可変、タプルは位置ごとに型が決まってるんだね。」
四国めたん「制約が強い場合はタプルを選びましょう。」
ずんだもん「柔軟に増減させたいならUnion配列が適しています。」
四国めたん「用途によって使い分けを意識しましょう。」
ずんだもん「最適なデータ構造を選んでね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: Union配列 */
const tokens: (string | number)[] = [];
tokens.push("start", 0);

/** Example 2: タプル */
type Response = [status: number, body: string];
const response: Response = [200, "OK"];

/** Example 3: 使い分け */
function asTuple(message: string, code: number): Response {
  return [code, message];
}
```
