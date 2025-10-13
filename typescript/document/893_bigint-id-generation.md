# #893 「IDの生成」

四国めたん「BigIntは分散IDやソート可能なIDの生成に便利です。」
ずんだもん「Snowflakeのタイムスタンプ＋ノードID＋シーケンスが典型だね。」
四国めたん「はい、ビットシフトで構造化されたIDを組み立てられます。」
ずんだもん「TypeScriptでもBigIntのビット操作で簡単に実装できるよ。」
四国めたん「桁数が大きくても精度を失わず表現できます。」
ずんだもん「ID生成でBigIntを活用して重複を防ごう！」
四国めたん「ノード間でシーケンスを管理する仕組みも合わせて設計してください。」
ずんだもん「分散システムで頼れる存在だよ！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: Snowflake風ID */
const EPOCH = 1_600_000_000_000n;
const NODE_ID = 0b101010n;
let sequence = 0n;
function nextId(): bigint {
  const timestamp = BigInt(Date.now()) - EPOCH;
  const id = (timestamp << 22n) | (NODE_ID << 12n) | sequence;
  sequence = (sequence + 1n) & 0xfffn;
  return id;
}

/** Example 2: 分解 */
function decode(id: bigint) {
  const seq = id & 0xfffn;
  const node = (id >> 12n) & 0x3fffn;
  const ts = (id >> 22n) + EPOCH;
  return { ts, node, seq };
}

/** Example 3: 使用 */
const id = nextId();
console.log(decode(id));
```
