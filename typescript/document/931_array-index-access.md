# #931 「インデックスアクセス」

四国めたん「配列要素はインデックスでアクセスします。」
ずんだもん「scores[0]みたいに書くやつだね。」
四国めたん「はい、0始まりで整数インデックスを指定します。」
ずんだもん「存在しないインデックスをアクセスするとundefinedが返るよ。」
四国めたん「型的には要素型が返りますがundefinedの可能性に注意しましょう。」
ずんだもん「インデックスアクセスの基本を押さえてね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 取得 */
const scores = [80, 90, 70];
const first = scores[0];

/** Example 2: 更新 */
scores[1] = 95;

/** Example 3: out-of-range */
const outside = scores[10]; // undefined
```
