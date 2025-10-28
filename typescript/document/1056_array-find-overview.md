# #1056 「Array.prototype.find()」

四国めたん「次はArray.prototype.findについて学びましょう。」
ずんだもん「条件に一致する最初の要素を返してくれるメソッドだね。」
四国めたん「見つからなければundefinedが返ります。」
ずんだもん「検索系メソッドの基本だから押さえておこう。」
四国めたん「findの概要を把握してから型の話に入ります。」
ずんだもん「素早く要素を探せるよ！」

---

## 📺 画面表示用コード

```typescript
const scores = [80, 92, 67];

/** Example 1: find */
const firstHigh = scores.find((score) => score >= 90);

/** Example 2: オブジェクト */
const users = [
  { id: "u1", active: false },
  { id: "u2", active: true },
];
const active = users.find((user) => user.active);

/** Example 3: 見つからない場合 */
const missing = scores.find((score) => score > 100); // undefined
```
