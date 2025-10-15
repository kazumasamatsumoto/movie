# #1041 「Array.prototype.reduce()」

四国めたん「次はArray.prototype.reduceを学びましょう。」
ずんだもん「配列を一つの値に畳み込むメソッドだね。」
四国めたん「はい、合計やオブジェクト構築など多用途に使えます。」
ずんだもん「コールバックと初期値を理解することが重要だよ。」
四国めたん「reduceの概要を押さえてから型の話に進みます。」
ずんだもん「強力なメソッドだから丁寧に見ていこう！」

---

## 📺 画面表示用コード

```typescript
const values = [1, 2, 3];

/** Example 1: 合計 */
const sum = values.reduce((acc, cur) => acc + cur, 0);

/** Example 2: 積 */
const product = values.reduce((acc, cur) => acc * cur, 1);

/** Example 3: 文字列結合 */
const joined = values.reduce((acc, cur) => `${acc}-${cur}`, "");
```
