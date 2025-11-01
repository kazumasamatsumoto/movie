# #863 「厳密比較 - false」

四国めたん「bigintとnumberを===で比べると常にfalseになります。」
ずんだもん「型が違うからだね。」
四国めたん「値が同じでも型が違えば一致しません。」
ずんだもん「厳密比較は型も含めた検証だから安全なんだよ。」
四国めたん「BigIntとnumberを混同しないためにも===を習慣化しましょう。」
ずんだもん「falseになる理由をチームで共有してね。」
四国めたん「型変換して比較したい場合は明示的に行います。」
ずんだもん「===で型ミスを防ごう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 厳密比較 */
const isSame = 100n === 100; // false

/** Example 2: 型揃えで比較 */
const equalAfterCast = Number(100n) === 100;

/** Example 3: ユーティリティ */
function equalsBigintNumber(big: bigint, num: number): boolean {
  return big === BigInt(num);
}
```
