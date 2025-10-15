# #1090 「includesまとめ」

四国めたん「includesのポイントをまとめましょう。」
ずんだん「存在チェックをbooleanで返し、NaNも検出できて、型の絞り込みはできないことを見たね。」
四国めたん「はい、indexOfとの違いやベストプラクティスも確認しました。」
ずんだん「次はその他の配列メソッドを見ていこう。」
四国めたん「includesを使いこなして存在判定を簡潔に書きましょう。」
ずんだん「配列操作の基礎が固まったね！」

---

## 📺 画面表示用コード

```typescript
const values = ["meta", "zunda", NaN];

const hasMeta = values.includes("meta");
const hasNaN = values.includes(NaN);
```
