# #1077 「使い分け」

四国めたん「someとeveryの使い分けを整理します。」
ずんだもん「条件を満たす要素があるか確認するときはsome、全て満たすか確認するときはeveryだね。」
四国めたん「はい、どちらも戻り値はbooleanで、短絡評価されます。」
ずんだん「否定形の条件は読みやすさに注意しよう。」
四国めたん「目的に応じて適切なメソッドを選択してください。」
ずんだん「役割を間違えずに使おう！」

---

## 📺 画面表示用コード

```typescript
const scores = [80, 92, 67];

const anyFail = scores.some((score) => score < 60);
const allPass = scores.every((score) => score >= 60);
```
