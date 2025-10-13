# #948 「初期化」

四国めたん「混合型配列の初期化ではUnion型に合致する値を並べます。」
ずんだもん「const tokens: (string | number)[] = ["GET", 200]; みたいな感じだね。」
四国めたん「はい、空配列の場合は型注釈が必須です。」
ずんだもん「後からpushする値もUnionのどちらかに収めよう。」
四国めたん「初期化時に型を明示しておくと安心です。」
ずんだもん「混合型配列の初期化ルールを押さえてね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 明示型 */
const tokens: (string | number)[] = ["GET", 200];

/** Example 2: 空配列 */
const log: Array<string | number> = [];
log.push("start");
log.push(Date.now());

/** Example 3: map */
const mapped = [1, 2, 3].map((value, i): string | number => (i % 2 ? value : `#${value}`));
```
