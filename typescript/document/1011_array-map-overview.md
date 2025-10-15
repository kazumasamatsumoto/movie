# #1011 「Array.prototype.map()」

四国めたん「今日はArray.prototype.mapについて学びましょう！」
ずんだもん「配列の各要素を変換して新しい配列を返してくれるメソッドだね。」
四国めたん「はい、元の配列は変更せず、同じ長さの新しい配列が返ります。」
ずんだもん「データ変換やビュー用の整形で大活躍だよ。」
四国めたん「mapの仕組みを理解して型安全な変換を書きましょう。」
ずんだもん「まずは概要から押さえてね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 基本 */
const scores = [80, 90, 70];
const labels = scores.map((score) => `score:${score}`);

/** Example 2: オブジェクト配列 */
const users = [
  { id: "u1", name: "meta" },
  { id: "u2", name: "zunda" },
];
const ids = users.map((user) => user.id);

/** Example 3: メソッドチェーン */
const doubledSorted = scores.map((score) => score * 2).sort((a, b) => a - b);
```
