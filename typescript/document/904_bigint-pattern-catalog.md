# #904 「パターン集」

四国めたん「BigInt活用パターンをカタログ化しましょう。」
ずんだもん「分散ID、固定小数点、暗号モジュラー演算、シリアライズ戦略が定番だね。」
四国めたん「各パターンをユーティリティとしてまとめておくと便利です。」
ずんだもん「プロジェクトごとに再利用しやすいテンプレートにしよう。」
四国めたん「パターン集をドキュメント化すると教育コストも下がります。」
ずんだもん「BigIntパターンを引き出しに入れてね！」
四国めたん「要件に応じてパターンを選択し、組み合わせて活用しましょう。」
ずんだもん「設計スピードが上がるよ！」

---

## 📺 画面表示用コード

```typescript
/** Pattern 1: 分散ID */
export const IdGenerator = {
  epoch: 1_600_000_000_000n,
  next(node: bigint, seq: bigint) {
    return ((BigInt(Date.now()) - this.epoch) << 22n) | (node << 12n) | seq;
  },
};

/** Pattern 2: 固定小数点 */
export const Money = {
  scale: 100n,
  fromNumber: (value: number) => BigInt(Math.round(value * Number(Money.scale))),
  toNumber: (value: bigint) => Number(value) / Number(Money.scale),
};

/** Pattern 3: シリアライズ */
export const Transport = {
  serialize: (value: bigint) => value.toString(),
  deserialize: (value: string) => BigInt(value),
};
```
