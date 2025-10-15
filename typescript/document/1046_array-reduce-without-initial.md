# #1046 「初期値なし - T型」

四国めたん「初期値を省略したreduceは最初の要素を初期値として使います。」
ずんだもん「だから結果型は要素型Tになるんだね。」
四国めたん「はい、配列が空だとTypeErrorになるので注意が必要です。」
ずんだもん「空配列がありえるなら必ず初期値を渡そう。」
四国めたん「初期値なしの挙動を理解して安全に使ってください。」
ずんだもん「デフォルト動作を覚えておこう！」

---

## 📺 画面表示用コード

```typescript
const values = [1, 2, 3];

/** Example 1: 初期値なし */
const total = values.reduce((acc, cur) => acc + cur);

/** Example 2: 空配列はエラー */
try {
  [].reduce((acc, cur) => acc + cur);
} catch (error) {
  console.error("TypeError", error);
}

/** Example 3: 明示的初期値推奨 */
const safeTotal = values.reduce((acc, cur) => acc + cur, 0);
```
