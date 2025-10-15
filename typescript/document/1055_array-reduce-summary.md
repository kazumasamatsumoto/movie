# #1055 「reduceまとめ」

四国めたん「reduceのポイントをまとめましょう。」
ずんだもん「初期値とアキュムレータ型、合計・オブジェクト構築・グループ化などの使い方を学んだね。」
四国めたん「はい、初期値を明示して型をコントロールするのが安全でした。」
ずんだもん「ベストプラクティスで読みやすさも確保しよう。」
四国めたん「次はfind系メソッドを見ていきます。」
ずんだもん「reduceを使いこなして集計を楽しもう！」

---

## 📺 画面表示用コード

```typescript
const numbers = [1, 2, 3];

/** Example 1: 合計 */
const sum = numbers.reduce((acc, cur) => acc + cur, 0);

/** Example 2: オブジェクト */
const byIndex = numbers.reduce<Record<number, number>>((acc, cur, index) => {
  acc[index] = cur;
  return acc;
}, {});

/** Example 3: グループ化 */
const grouped = numbers.reduce<Record<string, number[]>>((acc, cur) => {
  const key = cur % 2 === 0 ? "even" : "odd";
  (acc[key] ??= []).push(cur);
  return acc;
}, { even: [], odd: [] });
```
