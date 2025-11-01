# #839 「基本パターン」

四国めたん「bigint運用の基本パターンを3つ押さえましょう。」
ずんだもん「1つ目はIDの生成、2つ目は累計カウンタ、3つ目は桁溢れ防止だね。」
四国めたん「共通ユーティリティとしてまとめておくと便利です。」
ずんだもん「変換関数と組み合わせて型安全に扱おう！」
四国めたん「基本パターンをチームで共有するとミスを減らせます。」
ずんだもん「bigintを使う場面で再利用してね！」
四国めたん「設計パターンを活かして拡張しやすくしましょう。」
ずんだもん「BigIntの定番レシピを覚えてね！」

---

## 📺 画面表示用コード

```typescript
/** Pattern 1: ID生成 */
const ID_EPOCH = 1_600_000_000_000n;
function nextId(node: bigint, seq: bigint) {
  return (BigInt(Date.now()) - ID_EPOCH) << 12n | (node << 4n) | seq;
}

/** Pattern 2: 累計カウンタ */
const counter = {
  value: 0n,
  add(delta: bigint) {
    this.value += delta;
  },
};

/** Pattern 3: 桁溢れ防止 */
function addSafe(a: number, b: number): number | bigint {
  const sum = a + b;
  return Number.isSafeInteger(sum) ? sum : BigInt(a) + BigInt(b);
}
```
