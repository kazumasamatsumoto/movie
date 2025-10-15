# #1065 「find()とfilter()[0]の違い」

四国めたん「find()とfilter()[0]の違いも押さえておきましょう。」
ずんだもん「findは最初に一致した要素を見つけた時点で終了します。」
四国めたん「一方filter()[0]は全要素をチェックしてから最初の結果を取るので非効率です。」
ずんだもん「戻り値型もfindはT | undefined、filter()[0]はT | undefinedだけど副作用が大きいよ。」
四国めたん「単一要素を探すならfindを使ってください。」
ずんだもん「性能と可読性を意識して選ぼう！」

---

## 📺 画面表示用コード

```typescript
const values = [1, 2, 3, 4];

const viaFind = values.find((value) => value % 2 === 0);

const viaFilter = values.filter((value) => value % 2 === 0)[0];
```
