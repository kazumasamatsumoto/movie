# #1084 「indexOf()との違い」

四国めたん「includesとindexOfの違いを整理しましょう。」
ずんだもん「indexOfは見つかった位置を返して、見つからないと-1だったね。」
四国めたん「はい、存在チェックならincludesの方が読みやすくNaNも扱えます。」
ずんだん「位置が欲しいときはindexOf、真偽だけならincludesを使おう。」
四国めたん「目的に応じて適切に使い分けてください。」
ずんだん「コードの意図が伝わりやすくなるよ！」

---

## 📺 画面表示用コード

```typescript
const values = [1, 2, 3];

const hasTwo = values.includes(2); // true
const indexOfTwo = values.indexOf(2); // 1

const hasFour = values.includes(4); // false
const indexOfFour = values.indexOf(4); // -1
```
