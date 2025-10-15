# #1060 「findIndex()」

四国めたん「次にArray.prototype.findIndexを見ていきましょう。」
ずんだもん「条件に一致する要素のインデックスを返すメソッドだね。」
四国めたん「はい、見つからなければ-1が返ります。」
ずんだもん「インデックスが欲しいときはこちらを使おう。」
四国めたん「findとセットで覚えておきましょう。」
ずんだもん「位置情報を取得できて便利だよ！」

---

## 📺 画面表示用コード

```typescript
const scores = [80, 92, 67];

const index = scores.findIndex((score) => score >= 90); // 1

const missingIndex = scores.findIndex((score) => score > 100); // -1

if (index !== -1) {
  console.log(`Found at ${index}`);
}
```
