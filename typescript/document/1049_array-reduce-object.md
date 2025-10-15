# #1049 「オブジェクト構築」

四国めたん「reduceでオブジェクトを構築するパターンを見てみましょう。」
ずんだもん「配列をキーと値のマップに変換するやつだね。」
四国めたん「はい、アキュムレータにRecord型を使えば型安全に構築できます。」
ずんだもん「集計やインデックス作成に便利だよ。」
四国めたん「オブジェクト構築の定番パターンとして覚えてください。」
ずんだもん「整理されたデータを作れるね！」

---

## 📺 画面表示用コード

```typescript
const entries = [
  { id: "u1", name: "meta" },
  { id: "u2", name: "zunda" },
];

/** Example 1: Record */
const byId = entries.reduce<Record<string, string>>((acc, cur) => {
  acc[cur.id] = cur.name;
  return acc;
}, {});

/** Example 2: グルーピング */
const grouped = entries.reduce<Record<string, string[]>>((acc, cur) => {
  const initial = acc[cur.name] ?? [];
  acc[cur.name] = [...initial, cur.id];
  return acc;
}, {});

/** Example 3: Map */
const map = entries.reduce<Map<string, string>>((acc, cur) => acc.set(cur.id, cur.name), new Map());
```
