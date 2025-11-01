# #1070 「find系まとめ」

四国めたん「find系メソッドのポイントをまとめましょう。」
ずんだもん「findはT | undefined、findIndexはnumber、findLast系は末尾から検索、型述語で絞り込みもできたね。」
四国めたん「使い分けとランタイムサポートも確認しました。」
ずんだもん「戻り値のundefinedや-1に注意して安全に扱おう。」
四国めたん「次はsome/everyメソッドを見ていきます。」
ずんだもん「find系を使いこなして検索をスマートにしよう！」

---

## 📺 画面表示用コード

```typescript
const values = ["meta", "zunda", "meta"];

const first = values.find((value) => value === "meta");
const last = values.findLast?.((value) => value === "meta");

const firstIndex = values.findIndex((value) => value === "meta");
const lastIndex = values.findLastIndex?.((value) => value === "meta");
```
