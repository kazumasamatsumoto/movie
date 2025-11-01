# #767 「Symbol.iteratorの意味」

四国めたん「Symbol.iteratorはオブジェクトを反復可能にするためのフックです。」
ずんだもん「for...ofやスプレッド構文が使えるようになるんだよね。」
四国めたん「イテレータを返すメソッドを定義すればプロトコルに準拠します。」
ずんだもん「TypeScriptなら戻り値にIterator型を指定できるよ。」
四国めたん「配列以外のコレクションでも自然に扱えるのが利点です。」
ずんだもん「独自データ構造でも簡単にfor...of対応できるね。」
四国めたん「イテレータプロトコルの入り口としてSymbol.iteratorを理解しましょう。」
ずんだもん「フロントでもバックでも役に立つよ！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: イテレータ実装 */
class Range {
  constructor(private readonly start: number, private readonly end: number) {}
  [Symbol.iterator](): Iterator<number> {
    let current = this.start;
    return {
      next: () =>
        current < this.end
          ? { value: current++, done: false }
          : { value: undefined, done: true },
    };
  }
}

/** Example 2: for...of で利用 */
for (const value of new Range(0, 3)) {
  console.log(value);
}

/** Example 3: スプレッド構文 */
const values = [...new Range(5, 8)];
console.log(values); // [5, 6, 7]
```
