# #1051 「重複除去」

四国めたん「reduceを使って配列の重複を除去することもできます。」
ずんだもん「Setを使う方法もあるけど、reduceで手続き的に書くのもアリだね。」
四国めたん「アキュムレータに配列やSetを使って存在チェックを入れます。」
ずんだもん「データ整形の途中で重複排除したいときに便利だよ。」
四国めたん「重複除去パターンを押さえておきましょう。」
ずんだもん「ユースケースに合わせて使い分けよう！」

---

## 📺 画面表示用コード

```typescript
const tokens = ["a", "b", "a", "c"];

/** Example 1: 配列アキュムレータ */
const unique = tokens.reduce<string[]>((acc, cur) => {
  if (!acc.includes(cur)) acc.push(cur);
  return acc;
}, []);

/** Example 2: Setアキュムレータ */
const uniqueSet = tokens.reduce<Set<string>>((acc, cur) => acc.add(cur), new Set());

/** Example 3: 数値 */
const numbers = [1, 2, 2, 3];
const uniqueNumbers = numbers.reduce<number[]>((acc, cur) => {
  if (!acc.includes(cur)) acc.push(cur);
  return acc;
}, []);
```
