# #853 「明示的変換 - Number(bigint)」

四国めたん「bigintをnumberに変えるにはNumber関数を使います。」
ずんだもん「ただしNumber.MAX_SAFE_INTEGERを超えると精度が落ちるんだよね。」
四国めたん「変換前に安全範囲かどうかをチェックしましょう。」
ずんだもん「UI表示や外部APIとの連携でnumberに戻す場面があるよ。」
四国めたん「精度を失う場合は文字列で扱う方が安全です。」
ずんだもん「変換のリスクを理解して使おう！」
四国めたん「Numberへの変換は最小限に留めましょう。」
ずんだもん「安全変換でバグを防いでね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 基本変換 */
const big = 123n;
const num = Number(big);

/** Example 2: 安全チェック */
function toNumberSafe(value: bigint): number {
  if (value > BigInt(Number.MAX_SAFE_INTEGER) || value < BigInt(Number.MIN_SAFE_INTEGER)) {
    throw new Error("precision lost");
  }
  return Number(value);
}

/** Example 3: 文字列 fallback */
function toDisplay(value: bigint): string {
  return value <= BigInt(Number.MAX_SAFE_INTEGER) ? Number(value).toLocaleString() : value.toString();
}
```
