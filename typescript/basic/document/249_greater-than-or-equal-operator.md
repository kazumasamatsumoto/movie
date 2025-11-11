# #249 「以上演算子 - >=」

四国めたん「以上演算子について学びましょう!」
ずんだもん「>=は大なりイコールって読むんだよね!」
四国めたん「はい。左辺が右辺より大きいか、等しい場合にtrueになります。」
ずんだもん「10 >= 5も10 >= 10もtrueになるの?」
四国めたん「その通りです。等しい場合も含むのがポイントです。」
ずんだもん「最小値のチェックによく使われるんだね!」
四国めたん「年齢制限や資格条件など、境界値を含む判定に便利です。」
ずんだもん「>と>=の使い分けが大事だから、しっかり理解するのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 基本的な使用例 */
console.log(10 >= 5);   // true
console.log(10 >= 10);  // true
console.log(5 >= 10);   // false

/** Example 2: 型安全な比較関数 */
function isGreaterOrEqual(a: number, b: number): boolean {
  return a >= b;
}

/** Example 3: 最小値チェック */
const age: number = 18;
if (age >= 18) {
  console.log('成人です');
}
```
