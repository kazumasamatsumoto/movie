# #836 「ユースケース」

四国めたん「bigintの代表的なユースケースを整理しましょう。」
ずんだもん「暗号アルゴリズム、ブロックチェーン、分散IDが定番だね。」
四国めたん「はい、超大規模な計数や金融計算にも使われます。」
ずんだもん「時刻やログのナノ秒精度管理にも役立つよ。」
四国めたん「TypeScriptで型安全に大きな整数を扱えるとバグを防げます。」
ずんだもん「ユースケースを把握して採用場面を見極めよう！」
四国めたん「適用先を明確にするとBigIntの効果が最大化されます。」
ずんだもん「現場で役立つシーンを覚えてね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 分散ID */
const epoch = 1_620_000_000_000n;
const node = 0xFFn;
const sequence = 1234n;
const snowflake = (epoch << 22n) | (node << 12n) | sequence;

/** Example 2: 暗号計算 */
function modExp(base: bigint, exponent: bigint, mod: bigint): bigint {
  let result = 1n;
  let b = base % mod;
  let e = exponent;
  while (e > 0n) {
    if (e & 1n) result = (result * b) % mod;
    e >>= 1n;
    b = (b * b) % mod;
  }
  return result;
}

/** Example 3: 高精度タイムスタンプ */
const nanoseconds = BigInt(Date.now()) * 1_000_000n;
```
