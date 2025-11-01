# #879 「小数は使えない」

四国めたん「bigintは整数専用なので小数点を扱えません。」
ずんだもん「1.5nみたいなリテラルもエラーになるんだね。」
四国めたん「演算でも商は切り捨てです。」
ずんだもん「小数が必要ならnumberやdecimalライブラリを使おう。」
四国めたん「整数部分と小数部分を別のBigIntで管理する手もあります。」
ずんだもん「小数が出る計算では型設計を工夫しよう！」
四国めたん「限界を理解して適切な型を選択してください。」
ずんだもん「BigIntは整数に特化した武器だよ！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: リテラルエラー */
// const invalid = 1.5n; // SyntaxError

/** Example 2: 商の切り捨て */
console.log(5n / 2n); // 2n

/** Example 3: 固定小数点の例 */
const scale = 100n;
const amount = 12345n; // 123.45を100倍した整数
const divided = amount / scale; // 123n
const remainder = amount % scale; // 45n
```
