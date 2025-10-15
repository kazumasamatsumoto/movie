# #1074 「Array.prototype.every()」

四国めたん「続いてArray.prototype.everyを見ていきます。」
ずんだもん「すべての要素が条件を満たしたらtrueになるメソッドだね。」
四国めたん「はい、途中でfalseになった時点で終了します。」
ずんだん「全要素チェックに向いているよ。」
四国めたん「someと対になるメソッドとして覚えてください。」
ずんだん「条件が全て満たされているか確認しよう！」

---

## 📺 画面表示用コード

```typescript
const scores = [80, 92, 67];

const allPass = scores.every((score) => score >= 60); // true

const allHigh = scores.every((score) => score >= 90); // false
```
