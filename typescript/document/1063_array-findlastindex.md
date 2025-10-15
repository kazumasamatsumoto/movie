# #1063 「findLastIndex()」

四国めたん「findLastIndexは条件に一致する最後の要素のインデックスを返します。」
ずんだもん「見つからなければ-1で、末尾から検索するんだね。」
四国めたん「はい、逆方向の探索に最適です。」
ずんだもん「ランタイムサポートを確認してから使おう。」
四国めたん「find系のバリエーションを押さえておきましょう。」
ずんだもん「柔軟に検索できるね！」

---

## 📺 画面表示用コード

```typescript
const values = [1, 2, 3, 4, 5];

const lastEvenIndex = values.findLastIndex((value) => value % 2 === 0); // 3

const missingIndex = values.findLastIndex((value) => value > 10); // -1
```
