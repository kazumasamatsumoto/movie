# #1026 「Array.prototype.filter()」

四国めたん「続いてArray.prototype.filterを見ていきましょう。」
ずんだもん「条件に合った要素だけを残すメソッドだね。」
四国めたん「元の配列を変更せず、真になった要素だけで新しい配列を返します。」
ずんだもん「絞り込みの基本メソッドだからしっかり押さえよう。」
四国めたん「概要をおさえてから型の話に進みます。」
ずんだもん「filterで安全に要素を絞り込もう！」

---

## 📺 画面表示用コード

```typescript
const scores = [80, 92, 67];

/** Example 1: しきい値 */
const passed = scores.filter((score) => score >= 80);

/** Example 2: オブジェクト */
const users = [
  { id: "u1", active: true },
  { id: "u2", active: false },
];
const activeUsers = users.filter((user) => user.active);

/** Example 3: チェーン */
const doubledActive = activeUsers.map((user) => ({ ...user, tag: "active" }));
```
