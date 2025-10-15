# #1053 「実践例」

四国めたん「reduceの実践例として、購買履歴を集計してみましょう。」
ずんだもん「金額の合計とカテゴリ別の件数を一気に求める感じだね。」
四国めたん「はい、アキュムレータに複合オブジェクトを使って集計します。」
ずんだもん「reduceなら一回のループでまとめられるよ。」
四国めたん「実例を参考に複雑な集計ロジックを組んでみてください。」
ずんだもん「型を活かして安全に集計しよう！」

---

## 📺 画面表示用コード

```typescript
interface Purchase {
  userId: string;
  category: "book" | "music" | "game";
  amount: number;
}

const purchases: Purchase[] = [
  { userId: "u1", category: "book", amount: 1200 },
  { userId: "u2", category: "music", amount: 800 },
  { userId: "u1", category: "book", amount: 1500 },
];

interface Summary {
  total: number;
  counts: Record<Purchase["category"], number>;
}

const summary = purchases.reduce<Summary>((acc, purchase) => {
  acc.total += purchase.amount;
  acc.counts[purchase.category] += 1;
  return acc;
}, { total: 0, counts: { book: 0, music: 0, game: 0 } });

const byUser = purchases.reduce<Record<string, number>>((acc, purchase) => {
  acc[purchase.userId] = (acc[purchase.userId] ?? 0) + purchase.amount;
  return acc;
}, {});
```
