# #773 「Symbol.species」

四国めたん「Symbol.speciesは継承時にどのコンストラクタを返すか指定します。」
ずんだもん「Arrayのサブクラスでmapしたときに戻り型を制御できるんだね。」
四国めたん「はい、静的getterで親クラスを返せば普通の配列を得られます。」
ずんだもん「Promiseにもspeciesが定義されていてチェーン時のコンストラクタを決めてるよ。」
四国めたん「TypeScriptではstatic get [Symbol.species]()を定義します。」
ずんだもん「ライブラリを継承したときの互換性確保に役立つね。」
四国めたん「Symbol.speciesを活用して戻り値の型を調整しましょう。」
ずんだもん「コレクション拡張時の武器になるよ！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: Arrayサブクラス */
class MyList<T> extends Array<T> {
  static get [Symbol.species]() {
    return Array;
  }
}
const list = new MyList(1, 2, 3);
const mapped = list.map((x) => x * 2);
console.log(mapped instanceof MyList); // false
console.log(mapped instanceof Array); // true

/** Example 2: speciesで独自クラス維持 */
class FixedList<T> extends Array<T> {
  static get [Symbol.species]() {
    return this;
  }
}
const fixed = new FixedList(1, 2);
console.log(fixed.filter(Boolean) instanceof FixedList); // true

/** Example 3: Promiseのspecies */
class CustomPromise<T> extends Promise<T> {
  static get [Symbol.species]() {
    return Promise;
  }
}
new CustomPromise((resolve) => resolve(42))
  .then((v) => v)
  .then((v) => console.log(v));
```
