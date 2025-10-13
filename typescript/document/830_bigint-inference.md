# #830 「bigintの型推論」

四国めたん「bigintリテラルはconstで宣言するとリテラル型、letではbigint型に推論されます。」
ずんだもん「numberと同じで再代入可能かどうかで広がるんだね。」
四国めたん「はい、BigInt関数の戻り値もbigint型として推論されます。」
ずんだもん「ジェネリクスでもextends bigintで制約できるよ。」
四国めたん「推論を理解すると型注釈を最小限にできます。」
ずんだもん「型推論を活かしてbigintをスマートに扱おう！」
四国めたん「unique symbolとは別物なので区別しましょう。」
ずんだもん「推論ルールを押さえてね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: const推論 */
const CONST_BIG = 100n; // 型: 100n

/** Example 2: let推論 */
let variable = 100n; // 型: bigint
variable += 1n;

/** Example 3: 関数戻り値 */
function createBigInt(value: string): bigint {
  return BigInt(value);
}
```
