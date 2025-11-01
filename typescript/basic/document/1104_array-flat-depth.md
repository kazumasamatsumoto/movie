# #1104 「深さ指定」

四国めたん「flatは引数で深さを指定できます。」
ずんだん「flat(2)なら2段階平坦化するってことだね。」
四国めたん「深いネストを扱うときはdepthを調整しましょう。」
ずんだん「Infinityを渡せば全てのネストを平坦化できるよ。」
四国めたん「深さ指定の挙動を確認しておきましょう。」
ずんだん「必要な分だけ平坦化しよう！」

---

## 📺 画面表示用コード

```typescript
const nested = [1, [2, [3, [4]]]];

const flat1 = nested.flat();
const flat2 = nested.flat(2);
const flatAll = nested.flat(Infinity);
```
