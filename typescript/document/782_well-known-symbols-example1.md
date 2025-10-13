# #782 「実践例(1)」

四国めたん「Well-known Symbolsを組み合わせたコレクション例を見ましょう。」
ずんだもん「iteratorとtoStringTagを実装してデバッグしやすくするんだね。」
四国めたん「はい、Iterableにすればfor...ofで扱えます。」
ずんだもん「toStringTagがあればログが読みやすくなるよ。」
四国めたん「specifies speciesを使えば戻り型も調整できます。」
ずんだもん「カスタムコレクションのテンプレートになるね。」
四国めたん「Well-known Symbolsの協調を体感してください。」
ずんだもん「これで仕様を一気に身近にできるよ！」

---

## 📺 画面表示用コード

```typescript
class Collection<T> extends Array<T> {
  static get [Symbol.species]() {
    return Array;
  }

  [Symbol.toStringTag] = "Collection";

  [Symbol.iterator](): Iterator<T> {
    let index = 0;
    return {
      next: () =>
        index < this.length
          ? { value: this[index++], done: false }
          : { value: undefined, done: true },
    };
  }
}

const numbers = new Collection(1, 2, 3);
console.log(Object.prototype.toString.call(numbers));
console.log([...numbers]);
console.log(numbers.map((n) => n * 2) instanceof Array); // true
```
