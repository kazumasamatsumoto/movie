# #785 「Well-known Symbolsまとめ」

四国めたん「Well-known Symbolsは言語機能のフックでしたね。」
ずんだもん「iteratorやasyncIteratorで反復処理を拡張できたよ。」
四国めたん「toStringTagやtoPrimitiveでデバッグや変換もカスタマイズできます。」
ずんだもん「matchやreplaceを使えば文字列操作も柔軟になったね。」
四国めたん「強力なので目的とテストをセットで運用しましょう。」
ずんだもん「TypeScriptの型定義がサポートしてくれるのも心強いよ。」
四国めたん「次章ではシンボルとオブジェクトの連携を確認します。」
ずんだもん「Well-known Symbolsを武器に一段上の設計へ進もう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: iterator */
const iterable = {
  *[Symbol.iterator]() {
    yield "a";
    yield "b";
  },
};
console.log([...iterable]);

/** Example 2: toPrimitive */
const metric = {
  value: 42,
  [Symbol.toPrimitive](hint: "number" | "string") {
    return hint === "number" ? this.value : `${this.value}ms`;
  },
};
console.log(`${metric}`);

/** Example 3: asyncIterator */
const asyncIterable = {
  async *[Symbol.asyncIterator]() {
    yield "start";
  },
};
(async () => {
  for await (const item of asyncIterable) {
    console.log(item);
  }
})();
```
