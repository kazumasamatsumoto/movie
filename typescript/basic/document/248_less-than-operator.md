# #248 「小なり演算子 - <」

四国めたん「小なり演算子について学びましょう!」
ずんだもん「<を使うと、左側が右側より小さいかをチェックできるんだね!」
四国めたん「はい。大なり演算子の逆の働きをします。」
ずんだもん「5 < 10はtrueだけど、10 < 5はfalseになるよね?」
四国めたん「その通りです。等しい場合もfalseになります。」
ずんだもん「型安全な比較関数を作ることもできるの?」
四国めたん「もちろんです。isLessのような関数で可読性が上がります。」
ずんだもん「スコアの範囲チェックとかでよく使うから、しっかり覚えるのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 基本的な使用例 */
console.log(5 < 10);   // true
console.log(10 < 5);   // false
console.log(5 < 5);    // false

/** Example 2: 型安全な比較関数 */
function isLess(a: number, b: number): boolean {
  return a < b;
}

/** Example 3: 範囲チェック */
const score: number = 75;
if (score < 80) {
  console.log('合格ラインです');
}
```
