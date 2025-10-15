# #1017 「アロー関数」

四国めたん「mapではアロー関数を使うと簡潔に書けます。」
ずんだもん「value => value * 2 みたいに書けるんだね。」
四国めたん「はい、thisを使わない場合はアロー関数が定番です。」
ずんだもん「複雑な処理のときはブロックとreturnを使おう。」
四国めたん「アロー関数で読みやすいコールバックを書いてください。」
ずんだもん「短く書けるのが魅力だよ！」

---

## 📺 画面表示用コード

```typescript
const numbers = [1, 2, 3];

/** Example 1: ワンライナー */
const doubled = numbers.map((value) => value * 2);

/** Example 2: ブロック */
const withIndex = numbers.map((value, index) => {
  return `${index}:${value}`;
});

/** Example 3: オブジェクト返却 */
const objects = numbers.map((value) => ({ value }));
```
