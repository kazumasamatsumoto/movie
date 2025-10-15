# #1042 「型定義」

四国めたん「reduceの型定義もlib.d.tsで複数のオーバーロードが用意されています。」
ずんだもん「初期値ありと初期値なしでジェネリックが変わるんだね。」
四国めたん「はい、初期値ありは<U>(callback: (acc: U, value: T, index: number, array: T[]) => U, initialValue: U): Uです。」
ずんだもん「型定義を読めばアキュムレータ型の決まり方がわかるよ。」
四国めたん「libを確認して挙動を把握しましょう。」
ずんだもん「型定義から理解を深めてね！」

---

## 📺 画面表示用コード

```typescript
interface Array<T> {
  reduce(callbackfn: (previousValue: T, currentValue: T, currentIndex: number, array: T[]) => T): T;
  reduce(callbackfn: (previousValue: T, currentValue: T, currentIndex: number, array: T[]) => T, initialValue: T): T;
  reduce<U>(callbackfn: (previousValue: U, currentValue: T, currentIndex: number, array: T[]) => U, initialValue: U): U;
}

const values = [1, 2, 3];

const total = values.reduce((acc, cur) => acc + cur, 0);

const flattened = [[1], [2]].reduce<number[]>((acc, cur) => acc.concat(cur), []);
```
