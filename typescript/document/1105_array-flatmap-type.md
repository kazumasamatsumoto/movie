# #1105 「flatMap()の型」

四国めたん「Array.prototype.flatMapはmapとflatを組み合わせたメソッドです。」
ずんだん「型定義はflatMap<U, This = undefined>(callback: (value: T, index: number, array: T[]) => U | ReadonlyArray<U>, thisArg?: This): U[]だね。」
四国めたん「はい、コールバックが配列を返した場合に一段階フラット化します。」
ずんだん「map + flat(1)と同じ動きだけど1回で書けるよ。」
四国めたん「flatMapの型を理解して効果的に使ってください。」
ずんだん「複雑な変換を簡潔に記述できるね！」

---

## 📺 画面表示用コード

```typescript
const sentences = ["hello world", "type script"];

const words = sentences.flatMap((sentence) => sentence.split(" "));
```
