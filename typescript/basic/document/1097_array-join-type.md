# #1097 「join()の型」

四国めたん「Array.prototype.joinは配列を文字列に変換します。」
ずんだん「型定義はjoin(separator?: string): stringだね。」
四国めたん「要素型に関係なく戻り値はstringになります。」
ずんだん「separatorを指定しないとカンマ区切りになるよ。」
四国めたん「joinの型と挙動を押さえておきましょう。」
ずんだん「表示用フォーマットに便利だね！」

---

## 📺 画面表示用コード

```typescript
const values = ["meta", "zunda"];

const csv = values.join(",");
```
