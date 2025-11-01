# #1095 「splice()の型」

四国めたん「Array.prototype.spliceは破壊的メソッドです。」
ずんだん「型定義ではsplice(start: number, deleteCount?: number, ...items: T[]): T[]になってるね。」
四国めたん「削除された要素をT[]として返し、元の配列を変更します。」
ずんだん「変更を外部に通知するときは注意しよう。」
四国めたん「spliceの型と挙動を理解して使ってください。」
ずんだん「破壊的変更が必要な場面で使おう！」

---

## 📺 画面表示用コード

```typescript
const values = ["a", "b", "c"];

const removed = values.splice(1, 1, "x", "y");
// values: ["a", "x", "y", "c"], removed: ["b"]
```
