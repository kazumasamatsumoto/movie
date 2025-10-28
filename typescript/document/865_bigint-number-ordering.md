# #865 「bigintとnumberの大小比較」

四国めたん「<や>の比較ではbigintとnumberを混ぜても評価できます。」
ずんだもん「10n < 20はtrueになるんだね。」
四国めたん「numberがBigIntに変換されて比較されます。」
ずんだもん「ただしNumber.MAX_SAFE_INTEGER付近では精度に注意だよ。」
四国めたん「意図しない比較を避けるために型を揃えるのが無難です。」
ずんだもん「性能と読みやすさのためにも一貫した型で比較しよう！」
四国めたん「mixed比較は運用ルールを決めて慎重に扱いましょう。」
ずんだもん「比較前にtoBigIntやNumberで揃えてね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 混在比較 */
console.log(10n < 20); // true
console.log(20n > 10); // true

/** Example 2: 危険領域 */
const nearLimit = BigInt(Number.MAX_SAFE_INTEGER);
console.log(nearLimit + 2n > Number.MAX_SAFE_INTEGER + 1); // true だが精度注意

/** Example 3: 型揃え */
function compare(a: bigint, b: number): boolean {
  return a > BigInt(b);
}
```
