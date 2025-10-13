# #892 「ハッシュ計算」

四国めたん「ハッシュ計算ではBigIntが中間値として使われることがあります。」
ずんだもん「SHA系はバイナリだけど、Merkle treeのノード計算でBigIntに変換することもあるよね。」
四国めたん「はい、ビット演算で安全な累積を行うときに役立ちます。」
ずんだもん「TypeScriptでもhash = (hash * prime + charCode) % mod みたいな計算ができるよ。」
四国めたん「巨大なmodを扱うときはBigIntが欠かせません。」
ずんだもん「ハッシュ計算でBigIntを取り入れて衝突を減らそう！」
四国めたん「結果を文字列化して保存する戦略も忘れずに。」
ずんだもん「大規模データのハッシュでも精度を保とう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: シンプルローリングハッシュ */
function rollingHash(text: string, prime = 131n, mod = 2n ** 61n - 1n): bigint {
  let hash = 0n;
  for (const char of text) {
    hash = (hash * prime + BigInt(char.charCodeAt(0))) % mod;
  }
  return hash;
}

/** Example 2: Merkle node */
function merkleNode(left: bigint, right: bigint, mod = 2n ** 256n - 189n) {
  return (left ^ right) % mod;
}

/** Example 3: 保管 */
const digest = rollingHash("typescript");
const stored = digest.toString(16);
```
