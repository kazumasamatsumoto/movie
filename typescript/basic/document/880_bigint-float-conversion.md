# #880 「浮動小数点数との変換」

四国めたん「浮動小数点数との相互変換では精度に注意しましょう。」
ずんだもん「numberをBigIntにするときは整数かどうか検証が必要だよ。」
四国めたん「逆にBigIntをnumberにすると安全範囲を超えると丸められます。」
ずんだもん「小数部を保持したいならスケールを決めて固定小数点にする手があるね。」
四国めたん「変換関数を共通化しておくとミスを減らせます。」
ずんだもん「浮動小数点との橋渡しを丁寧に設計しよう！」
四国めたん「精度要件を満たすかどうかを確認してから変換してください。」
ずんだもん「BigIntとfloatの距離を意識してね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: number→bigint */
function toBigint(value: number): bigint {
  if (!Number.isInteger(value)) throw new Error("integer required");
  return BigInt(value);
}

/** Example 2: bigint→number */
function toNumber(value: bigint): number {
  const num = Number(value);
  if (!Number.isSafeInteger(num)) throw new Error("precision lost");
  return num;
}

/** Example 3: 固定小数点 */
function toFixedBigint(value: number, scale = 100n): bigint {
  return BigInt(Math.round(value * Number(scale)));
}
```
