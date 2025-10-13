# #974 「関係」

四国めたん「(string | number)[]とstring[] | number[]はサブタイプ関係にはありません。」
ずんだもん「お互いに代入できないんだね。」
四国めたん「はい、構造が異なるため互換性はありません。」
ずんだもん「型変換するときは明示的にmapやガードを使おう。」
四国めたん「関係性を理解して安易な代入を避けましょう。」
ずんだもん「型整合性を守ってね！」

---

## 📺 画面表示用コード

```typescript
const mixed: (string | number)[] = ["ok", 200];
const exclusive: string[] | number[] = ["ok"];

// mixed = exclusive; // エラー
// exclusive = mixed; // エラー

/** Example 1: 変換 */
const asExclusive: string[] | number[] = typeof mixed[0] === "string" ? ["ok"] : [1];

/** Example 2: map */
const toStrings = mixed.map(String); // string[]

/** Example 3: 明示的変換 */
function toExclusive(value: (string | number)[]): string[] | number[] {
  return value.every((item) => typeof item === "number") ? value as number[] : value.map(String);
}
```
