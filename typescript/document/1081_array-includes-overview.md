# #1081 「Array.prototype.includes()」

四国めたん「次はArray.prototype.includesを学びましょう。」
ずんだん「配列に特定の値が含まれているか判定するメソッドだね。」
四国めたん「はい、見つかればtrue、なければfalseを返します。」
ずんだもん「NaNも正しく判定できるのがポイントだよ。」
四国めたん「includesで存在判定を簡潔に書きましょう。」
ずんだん「基本のAPIだからしっかり覚えてね！」

---

## 📺 画面表示用コード

```typescript
const tags = ["ts", "js", "node"];

const hasTs = tags.includes("ts");

const hasReact = tags.includes("react");
```
