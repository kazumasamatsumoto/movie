# #828 「BigInt()関数 - 文字列」

四国めたん「BigInt関数に文字列を渡すとbigint値に変換できます。」
ずんだもん「BigInt("1234567890")みたいに書くんだね。」
四国めたん「文字列は整数である必要があります。」
ずんだもん「進数表記や16進も受け付けるの？」
四国めたん「0b、0o、0xの接頭辞を付けた文字列も変換できます。」
ずんだもん「APIから受け取った巨大な文字列をBigIntに変えられるのが便利だよ。」
四国めたん「変換時の例外ハンドリングも忘れずに。」
ずんだもん「文字列入力から安全にBigIntを作ろう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 文字列から変換 */
const fromString = BigInt("12345678901234567890");

/** Example 2: 16進数 */
const hex = BigInt("0xFF_FF_FF_FF_FF_FF_FF_FF");

/** Example 3: 例外処理 */
function parseBigInt(input: string): bigint | null {
  try {
    return BigInt(input);
  } catch {
    return null;
  }
}
```
