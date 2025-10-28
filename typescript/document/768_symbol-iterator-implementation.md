# #768 「Symbol.iteratorの実装」

四国めたん「Symbol.iteratorはジェネレーターで実装すると簡潔です。」
ずんだもん「function*を使えばイテレータオブジェクトを自動で返してくれるんだね。」
四国めたん「yieldで要素を順に返すだけです。」
ずんだもん「手動でnext関数を書きたい場合もreturnでdone:trueを返せばOKだよ。」
四国めたん「TypeScriptではIteratorResult型が補完されるので安全です。」
ずんだもん「実装方法を覚えて独自コレクションに対応させよう！」
四国めたん「テストでfor...ofが期待通りになるか確認してください。」
ずんだもん「実装パターンを手に入れたら応用は自由だよ！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: ジェネレーター実装 */
class Fib {
  constructor(private readonly limit: number) {}
  *[Symbol.iterator]() {
    let a = 0;
    let b = 1;
    while (a <= this.limit) {
      yield a;
      [a, b] = [b, a + b];
    }
  }
}

/** Example 2: 手動イテレータ */
class Countdown {
  constructor(private value: number) {}
  [Symbol.iterator](): Iterator<number> {
    return {
      next: (): IteratorResult<number> =>
        this.value >= 0
          ? { value: this.value--, done: false }
          : { value: undefined, done: true },
    };
  }
}

/** Example 3: テスト */
console.log([...new Fib(10)]); // [0,1,1,2,3,5,8]
console.log([...new Countdown(3)]); // [3,2,1,0]
```
