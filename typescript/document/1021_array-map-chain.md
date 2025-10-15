# #1021 「チェーン」

四国めたん「mapはfilterやreduceなどとチェーンして使うことが多いです。」
ずんだもん「変換してから絞り込むとか、整形して合計を取るとかだね。」
四国めたん「はい、チェーンすると可読性が上がります。」
ずんだもん「ただし途中の型がどう変わるか意識しよう。」
四国めたん「チェーンで型を繋ぎながら処理を構築してください。」
ずんだもん「パイプライン風に書けて気持ちいいよ！」

---

## 📺 画面表示用コード

```typescript
const scores = [80, 90, 70];

/** Example 1: map + filter */
const highScores = scores
  .map((score) => ({ score, passed: score >= 80 }))
  .filter((entry) => entry.passed);

/** Example 2: map + reduce */
const average = scores
  .map((score) => score * 1.1)
  .reduce((acc, cur, _, array) => acc + cur / array.length, 0);

/** Example 3: flatMapチェーン */
const tokens = scores
  .map((score) => (score >= 80 ? [`pass-${score}`] : []))
  .flat();
```
