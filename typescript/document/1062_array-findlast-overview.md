# #1062 「findLast()」

四国めたん「ES2023で導入されたfindLastも押さえておきましょう。」
ずんだもん「条件に一致する最後の要素を返すメソッドだね。」
四国めたん「はい、見つからなければundefinedです。」
ずんだもん「末尾から検索するので逆順の探索に便利だよ。」
四国めたん「対応ランタイムか確認した上で活用してください。」
ずんだもん「新しいAPIも使いこなそう！」

---

## 📺 画面表示用コード

```typescript
const values = [1, 2, 3, 4, 5];

const lastEven = values.findLast((value) => value % 2 === 0); // 4

const missing = values.findLast((value) => value > 10); // undefined
```
