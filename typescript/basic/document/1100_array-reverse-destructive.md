# #1100 「破壊的変更」

四国めたん「reverseは破壊的メソッドなので元の配列を直接変更します。」
ずんだん「コピーしてからreverseしたい場合はスプレッドで複製してから使うんだね。」
四国めたん「const reversed = [...values].reverse() のように書きます。」
ずんだん「副作用を避けたいときの定番パターンだよ。」
四国めたん「破壊的メソッドを使う前に影響範囲を確認しましょう。」
ずんだん「後続処理に影響がないかも気をつけてね！」

---

## 📺 画面表示用コード

```typescript
const values = [1, 2, 3];

const reversedImmutable = [...values].reverse();

// valuesはそのまま
```
