# #250 「以下演算子 - <=」

四国めたん「以下演算子について学びましょう!」
ずんだもん「<=は小なりイコールって読むんだね!」
四国めたん「はい。左辺が右辺より小さいか、等しい場合にtrueになります。」
ずんだもん「5 <= 10も5 <= 5もtrueになるの?」
四国めたん「その通りです。等しい場合も含むのが特徴です。」
ずんだもん「最大値のチェックによく使われるんだね!」
四国めたん「スコアの上限や在庫数の確認など、上限値を含む判定に便利です。」
ずんだもん「<と<=の違いをしっかり理解して使い分けるのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 基本的な使用例 */
console.log(5 <= 10);   // true
console.log(5 <= 5);    // true
console.log(10 <= 5);   // false

/** Example 2: 型安全な比較関数 */
function isLessOrEqual(a: number, b: number): boolean {
  return a <= b;
}

/** Example 3: 最大値チェック */
const score: number = 100;
if (score <= 100) {
  console.log('有効なスコアです');
}
```
