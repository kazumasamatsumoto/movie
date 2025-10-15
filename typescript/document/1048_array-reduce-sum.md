# #1048 「合計値 - number[]からnumber」

四国めたん「reduceの代表的な使い道は合計値計算です。」
ずんだもん「number[]をreduceで畳み込めば簡単に合計が出せるんだね。」
四国めたん「はい、初期値0を渡してacc + curで足し合わせます。」
ずんだもん「要素がないときにも0が返るように初期値を設定しよう。」
四国めたん「合計値パターンをしっかり覚えておきましょう。」
ずんだもん「最もベーシックな使い方だね！」

---

## 📺 画面表示用コード

```typescript
const scores = [80, 92, 67];

/** Example 1: 合計 */
const total = scores.reduce((acc, cur) => acc + cur, 0);

/** Example 2: 平均 */
const average = scores.reduce((acc, cur, _, array) => acc + cur / array.length, 0);

/** Example 3: 最大値 */
const max = scores.reduce((acc, cur) => Math.max(acc, cur));
```
