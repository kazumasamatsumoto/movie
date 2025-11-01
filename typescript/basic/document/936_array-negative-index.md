# #936 「負のインデックス」

四国めたん「atメソッドは負のインデックスにも対応しています。」
ずんだもん「arr.at(-1)で末尾要素が取れるんだね。」
四国めたん「従来はarr[arr.length - 1]と書く必要がありました。」
ずんだもん「読みやすさが改善されるから積極的に使いたいね。」
四国めたん「型もT | undefinedなので安全に扱えます。」
ずんだもん「負のインデックス活用でコードをスッキリさせよう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 最後の要素 */
const stack = ["init", "load", "done"];
const last = stack.at(-1);

/** Example 2: 最後から2番目 */
const secondLast = stack.at(-2);

/** Example 3: 従来の書き方 */
const legacyLast = stack[stack.length - 1];
```
