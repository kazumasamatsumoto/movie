# #1043 「reduce<U>(callback, initialValue: U): U」

四国めたん「初期値ありのreduceはreduce<U>(callback, initialValue: U): Uという形です。」
ずんだもん「アキュムレータ型Uを自由に決められるんだね。」
四国めたん「初期値を渡すことでU型の結果を得られます。」
ずんだもん「配列からオブジェクトやMapを作るときに便利だよ。」
四国めたん「シグネチャを理解して初期値を正しく設定しましょう。」
ずんだもん「型の自由度が高まるね！」

---

## 📺 画面表示用コード

```typescript
const entries = [
  { key: "a", value: 1 },
  { key: "b", value: 2 },
];

/** Example 1: オブジェクト構築 */
const mapObject = entries.reduce<Record<string, number>>((acc, cur) => {
  acc[cur.key] = cur.value;
  return acc;
}, {});

/** Example 2: Set */
const uniqueIds = entries.reduce<Set<string>>((acc, cur) => acc.add(cur.key), new Set());

/** Example 3: 文字列 */
const csv = entries.reduce((acc, cur) => `${acc}${cur.key},${cur.value}\n`, "");
```
