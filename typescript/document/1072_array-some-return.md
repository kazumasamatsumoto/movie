# #1072 「戻り値型 - boolean」

四国めたん「someの戻り値は常にbooleanです。」
ずんだもん「trueかfalseだけだから扱いやすいね。」
四国めたん「はい、短絡評価されることも覚えておきましょう。」
ずんだん「条件に一致した瞬間にtrueで抜けるんだね。」
四国めたん「戻り値型を意識してロジックを組み立ててください。」
ずんだん「if文との相性がいいよ！」

---

## 📺 画面表示用コード

```typescript
const values = [1, 2, 3, 4];

const hasEven = values.some((value) => value % 2 === 0);

if (hasEven) {
  console.log("even exists");
}
```
