# #1079 「ベストプラクティス」

四国めたん「some/everyを使うときのベストプラクティスをまとめます。」
ずんだもん「戻り値はbooleanなので条件分岐に直接使い、否定条件は読みやすく書くんだったね。」
四国めたん「はい、結果を変数に格納して意味を明示すると可読性が上がります。」
ずんだもん「重い計算を行う場合はコールバック内で注意しよう。」
四国めたん「ベストプラクティスを守って判定処理を安全に書いてください。」
ずんだもん「シンプルに書くのがコツだよ！」

---

## 📺 画面表示用コード

```typescript
const items = ["meta", "zunda", ""];

const hasEmpty = items.some((item) => item === "");
const allFilled = items.every((item) => item !== "");

if (hasEmpty) {
  console.warn("empty item detected");
}
```
