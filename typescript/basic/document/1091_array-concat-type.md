# #1091 「concat()の型」

四国めたん「まずはArray.prototype.concatの型を確認しましょう。」
ずんだん「同じ要素型を結合して新しい配列を返すメソッドだね。」
四国めたん「型定義ではconcat(...items: ConcatArray<T>[]): T[]の形になっています。」
ずんだん「複数の配列や値をまとめたいときに使えるよ。」
四国めたん「concatの型を押さえておきましょう。」
ずんだん「元の配列を破壊しないのもポイントだね！」

---

## 📺 画面表示用コード

```typescript
const base = [1, 2];

const merged = base.concat([3, 4]);

const withValue = base.concat(5);
```
