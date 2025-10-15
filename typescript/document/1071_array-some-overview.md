# #1071 「Array.prototype.some()」

四国めたん「次はArray.prototype.someを学びましょう。」
ずんだもん「条件を満たす要素が1つでもあればtrueを返すメソッドだね。」
四国めたん「はい、短絡評価され、booleanが戻ります。」
ずんだん「存在チェックやバリデーションに使いやすいよ。」
四国めたん「someの基本を押さえておきましょう。」
ずんだん「配列の中に条件を満たすものがあるか調べよう！」

---

## 📺 画面表示用コード

```typescript
const scores = [80, 92, 67];

const hasHighScore = scores.some((score) => score >= 90); // true

const hasFail = scores.some((score) => score < 60); // false
```
