# #835 「特性」

四国めたん「bigintの主な特性を押さえましょう。」
ずんだもん「整数専用、任意精度、四則演算や比較がサポートされてるね。」
四国めたん「そうです。NaNやInfinityが存在せず、Math関数は使えません。」
ずんだもん「ビット演算も利用できる点が便利だよ。」
四国めたん「JSONに直接シリアライズできない点も重要です。」
ずんだもん「特性を理解して適切なユースケースに当てよう！」
四国めたん「制約込みでbigintの設計を考えてください。」
ずんだもん「BigIntの性格を覚えてね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: NaN/Infinityは存在しない */
// console.log(BigInt(NaN)); // RangeError

/** Example 2: ビット演算 */
const flags = 0b1010n & 0b1100n;

/** Example 3: JSONに含める場合 */
const payload = { value: flags.toString() };
```
