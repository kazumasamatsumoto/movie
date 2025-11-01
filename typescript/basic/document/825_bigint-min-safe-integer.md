# #825 「MIN_SAFE_INTEGER」

四国めたん「Number.MIN_SAFE_INTEGERは安全に表現できる最小の整数です。」
ずんだもん「-9,007,199,254,740,991だね。」
四国めたん「これより小さい値は丸められてしまいます。」
ずんだもん「BigIntなら負の大きな値も余裕で扱えるよ。」
四国めたん「境界を把握してBigIntへ切り替える判断をしましょう。」
ずんだもん「負のIDや残高計算でも役立つね。」
四国めたん「MIN_SAFE_INTEGERはBigInt適用のもう一つの指標です。」
ずんだもん「下限値も意識して精度を守ろう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 下限 */
console.log(Number.MIN_SAFE_INTEGER); // -9007199254740991

/** Example 2: 下限を下回る */
const below = Number.MIN_SAFE_INTEGER - 1;
console.log(below === below - 1); // true: 精度喪失

/** Example 3: BigIntで表現 */
const hugeNegative = BigInt(Number.MIN_SAFE_INTEGER) - 10_000n;
console.log(hugeNegative);
```
