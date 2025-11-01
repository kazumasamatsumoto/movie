# #823 「必要性」

四国めたん「なぜBigIntが必要なのか確認しましょう。」
ずんだもん「numberは53bitまでしか整数精度が保証されないんだよね。」
四国めたん「金融や暗号、分散IDのように巨大な整数を扱うと精度が失われます。」
ずんだもん「BigIntなら丸めなしで計算できるから安心だよ。」
四国めたん「データベースの巨大IDやブロックチェーンの値を安全に取り扱えます。」
ずんだもん「現場での精度問題をBigIntで解決しよう！」
四国めたん「必要性を理解すると採用判断がしやすくなります。」
ずんだもん「安全な整数演算のためにBigIntを選ぼう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 精度喪失の例 */
const maxSafe = Number.MAX_SAFE_INTEGER;
console.log(maxSafe + 1 === maxSafe + 2); // true: 精度喪失

/** Example 2: BigIntなら安全 */
const precise = 9_007_199_254_740_992n;
console.log(precise + 1n === precise + 2n); // false

/** Example 3: UUIDの計算 */
const shardId: bigint = 0b1111_0000_1111n;
const sequence: bigint = 1234567890123n;
const snowflake = (shardId << 32n) | sequence;
```
