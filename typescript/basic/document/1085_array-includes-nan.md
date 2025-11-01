# #1085 「NaN検索」

四国めたん「includesはNaNを正しく検出できます。」
ずんだん「indexOfではNaNが見つからなかったんだよね。」
四国めたん「SameValueZero比較を採用しているためNaN同士も一致します。」
ずんだん「数値データの検証で役立つよ。」
四国めたん「NaN検索の違いを覚えておきましょう。」
ずんだん「バグを防げるポイントだね！」

---

## 📺 画面表示用コード

```typescript
const values = [1, NaN, 3];

const hasNaN = values.includes(NaN); // true
const indexOfNaN = values.indexOf(NaN); // -1
```
