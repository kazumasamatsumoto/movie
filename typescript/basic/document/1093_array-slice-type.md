# #1093 「slice()の型」

四国めたん「次はArray.prototype.sliceの型を確認します。」
ずんだん「部分配列を取り出すメソッドだね。」
四国めたん「型定義ではslice(start?: number, end?: number): T[]の形です。」
ずんだん「元の配列を変更せず、同じ要素型の配列を返すんだね。」
四国めたん「sliceの基本を押さえておきましょう。」
ずんだん「イミュータブルな抜き出しに便利だよ！」

---

## 📺 画面表示用コード

```typescript
const values = ["meta", "zunda", "guest"];

const firstTwo = values.slice(0, 2);
```
