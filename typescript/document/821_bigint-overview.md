# #821 「bigint型とは」

四国めたん「TypeScript v5.9のbigint型について学びましょう！」
ずんだもん「numberとどう違うの？」
四国めたん「bigintは任意精度の整数を扱えるプリミティブで、末尾にnを付けてリテラルを書きます。」
ずんだもん「だからオーバーフローを気にせず巨大な値を扱えるんだね。」
四国めたん「整数演算に特化しており浮動小数は扱いません。」
ずんだもん「IDや暗号など大きい整数を扱う場面で活躍しそうだよ。」
四国めたん「TypeScriptではbigint型として静的チェックされます。」
ずんだもん「大きな整数の味方として覚えておこう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: bigintリテラル */
const huge: bigint = 9_223_372_036_854_775_807n;

/** Example 2: BigInt関数 */
const fromString = BigInt("12345678901234567890");

/** Example 3: 型注釈 */
let balance: bigint = 0n;
balance += 1000n;
```
