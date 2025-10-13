# #845 「剰余 - a % b」

四国めたん「剰余演算は%で、bigint同士の余りを求めます。」
ずんだもん「ハッシュテーブルのインデックスにも使えるね。」
四国めたん「はい、mod演算は暗号や数論で重要です。」
ずんだもん「負数にも対応しているから符号に注意して扱おう。」
四国めたん「剰余を返す関数を共通化しておくと便利です。」
ずんだもん「BigIntの剰余で大きな数の計算を安定させよう！」
四国めたん「商との組み合わせで割り算結果を完全に把握できます。」
ずんだもん「modの基本を押さえてね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 基本剰余 */
const remainder = 10n % 3n; // 1n

/** Example 2: 正規化 */
function mod(a: bigint, b: bigint): bigint {
  const r = a % b;
  return r >= 0n ? r : r + b;
}

/** Example 3: ハッシュ */
function bucket(id: bigint, size: bigint) {
  return mod(id, size);
}
```
