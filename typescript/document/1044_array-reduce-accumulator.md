# #1044 「アキュムレータ型」

四国めたん「reduceのアキュムレータ型は初期値で決まります。」
ずんだもん「初期値をRecordにすればアキュムレータもRecordになるんだね。」
四国めたん「コールバックの戻り値も同じ型に揃える必要があります。」
ずんだもん「アキュムレータ型を意識して設計しよう。」
四国めたん「型の一貫性がreduce成功の鍵です。」
ずんだもん「型安全なアキュムレータを使ってね！」

---

## 📺 画面表示用コード

```typescript
const entries = ["meta", "zunda"];

/** Example 1: Record */
const indexMap = entries.reduce<Record<string, number>>((acc, cur, index) => {
  acc[cur] = index;
  return acc;
}, {});

/** Example 2: Map */
const indexMap2 = entries.reduce<Map<string, number>>((acc, cur, index) => acc.set(cur, index), new Map());

/** Example 3: カスタム型 */
interface Stats { count: number; names: string[] }
const stats = entries.reduce<Stats>((acc, cur) => ({
  count: acc.count + 1,
  names: [...acc.names, cur],
}), { count: 0, names: [] });
```
