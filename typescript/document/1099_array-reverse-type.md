# #1099 「reverse()の型」

四国めたん「Array.prototype.reverseは配列を逆順に並べ替えます。」
ずんだん「型定義はreverse(): T[]だね。」
四国めたん「はい、戻り値は同じ配列参照で、破壊的メソッドです。」
ずんだん「元の配列が変更される点に注意しよう。」
四国めたん「reverseの型と挙動を押さえてください。」
ずんだん「コピーしてから使うのもアリだね！」

---

## 📺 画面表示用コード

```typescript
const values = [1, 2, 3];

const reversed = values.reverse();
// values === reversed
```
