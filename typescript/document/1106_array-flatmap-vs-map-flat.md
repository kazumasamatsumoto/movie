# #1106 「flatMap()とmap().flat()」

四国めたん「flatMapはmap().flat(1)と同等の挙動を1ステップで提供します。」
ずんだん「mapで配列を返して、その後flat(1)で平坦化する手間が省けるんだね。」
四国めたん「はい、可読性とパフォーマンスの両面でメリットがあります。」
ずんだん「ただしflatMapも破壊的ではなく新しい配列を返すよ。」
四国めたん「flatMapとmap().flat()の使い分けを覚えてください。」
ずんだん「コードをスッキリ書けるね！」

---

## 📺 画面表示用コード

```typescript
const sentences = ["hello world", "type script"];

const wordsViaFlatMap = sentences.flatMap((sentence) => sentence.split(" "));

const wordsViaMapFlat = sentences.map((sentence) => sentence.split(" ")).flat();
```
