# #766 「Well-known Symbolsとは」

四国めたん「Well-known SymbolsはJavaScript仕様で予約されたシンボル群です。」
ずんだもん「Symbol.iteratorやSymbol.toStringTagみたいなやつだね。」
四国めたん「はい、言語の挙動をカスタマイズするフックとして使われます。」
ずんだもん「TypeScriptでも型定義が用意されてるから安心だよ。」
四国めたん「知っているとフレームワークの内部動作が読み解けます。」
ずんだもん「自前のコレクションやAPIを標準プロトコルに合わせられるね。」
四国めたん「Well-known Symbolsを学んで言語機能を拡張しましょう。」
ずんだもん「仕組みを押さえれば動的な挙動も怖くないよ！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: Symbol.iterator */
const iterable = {
  items: [1, 2, 3],
  [Symbol.iterator]() {
    return this.items.values();
  },
};

/** Example 2: Symbol.toStringTag */
const tagged = {
  [Symbol.toStringTag]: "CustomCollection",
};
console.log(Object.prototype.toString.call(tagged)); // [object CustomCollection]

/** Example 3: Symbol.toPrimitive */
const amount = {
  value: 100,
  [Symbol.toPrimitive](hint: "number" | "string") {
    return hint === "number" ? this.value : `$${this.value}`;
  },
};
console.log(+amount); // 100
```
