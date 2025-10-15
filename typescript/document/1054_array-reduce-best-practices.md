# #1054 「ベストプラクティス」

四国めたん「reduceを使うときのベストプラクティスをまとめます。」
ずんだもん「初期値を必ず指定する、アキュムレータ型をわかりやすくする、純粋関数にする、だったね。」
四国めたん「はい、処理が複雑になりすぎる場合は他のメソッドとの組み合わせを検討します。」
ずんだもん「ユーティリティ関数に切り出すとテストしやすくなるよ。」
四国めたん「ベストプラクティスを守って安全なreduceを書いてください。」
ずんだもん「読みやすさと型安全性を大事にしよう！」

---

## 📺 画面表示用コード

```typescript
const values = [1, 2, 3];

/** Example 1: 初期値を明示 */
const sum = values.reduce((acc, cur) => acc + cur, 0);

/** Example 2: 純粋関数化 */
const toMap = <T>(items: T[], mapper: (acc: Map<string, T>, cur: T) => Map<string, T>) =>
  items.reduce(mapper, new Map<string, T>());

/** Example 3: 抽出 */
function groupBy<T>(items: T[], key: (item: T) => string) {
  return items.reduce<Record<string, T[]>>((acc, item) => {
    const k = key(item);
    (acc[k] ??= []).push(item);
    return acc;
  }, {});
}
```
