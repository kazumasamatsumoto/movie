# #972 「型推論」

四国めたん「配列とUnion型の組み合わせでもTypeScriptの推論が働きます。」
ずんだもん「["ok", 200]は(string | number)[]に推論されるんだね。」
四国めたん「はい、文字列配列か数値配列のUnionも初期化時に推論されます。」
ずんだもん「ただし意図しない型になったら注釈で補正しよう。」
四国めたん「推論結果を確認しながら設計してください。」
ずんだもん「推論と注釈のバランスを取ってね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 推論 */
const mixed = ["ok", 200]; // (string | number)[]

/** Example 2: 排他的 */
const exclusive = Math.random() > 0.5 ? ["a"] : [1, 2]; // string[] | number[]

/** Example 3: 補正 */
const ensureNumbers: number[] = exclusive.filter((value): value is number => typeof value === "number");
```
