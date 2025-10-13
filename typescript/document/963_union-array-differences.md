# #963 「2つの表記の違い」

四国めたん「(string | number)[]とstring[] | number[]の違いを整理しましょう。」
ずんだもん「前者は混在、後者は排他的ってことだね。」
四国めたん「はい、どちらもUnionですがレベルが違います。」
ずんだもん「実装前にどちらが意図に合うか確認しよう。」
四国めたん「データ構造とAPI仕様を考えて記法を選んでください。」
ずんだもん「違いを理解してミスを減らそう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 混在 */
const mixed: (string | number)[] = ["ok", 200];

/** Example 2: 排他的 */
const exclusive: string[] | number[] = Math.random() > 0.5 ? ["a"] : [1, 2, 3];

/** Example 3: 型比較 */
type Mixed = (string | number)[];
type Exclusive = string[] | number[];
```
