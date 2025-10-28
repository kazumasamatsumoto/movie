# #769 「イテレータプロトコル」

四国めたん「イテレータプロトコルはnext()で{ value, done }を返す契約です。」
ずんだもん「doneがtrueになったら反復が終わるんだよね。」
四国めたん「Symbol.iteratorはそのイテレータを返すメソッドです。」
ずんだもん「手動でnextを呼べば処理を細かく制御できるよ。」
四国めたん「ジェネレーターもこのプロトコルを満たしています。」
ずんだもん「プロトコルを理解するとfor...ofの裏側が見えるね。」
四国めたん「TypeScriptでIteratorResult型を使うと安全です。」
ずんだもん「プロトコルを押さえて高度な反復処理に挑戦しよう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 手作りイテレータ */
function createIterator(limit: number): Iterator<number> {
  let current = 0;
  return {
    next(): IteratorResult<number> {
      return current < limit
        ? { value: current++, done: false }
        : { value: undefined, done: true };
    },
  };
}

/** Example 2: nextの制御 */
const iterator = createIterator(2);
console.log(iterator.next()); // { value: 0, done: false }
console.log(iterator.next()); // { value: 1, done: false }
console.log(iterator.next()); // { value: undefined, done: true }

/** Example 3: Symbol.iteratorとの連携 */
const iterable = {
  [Symbol.iterator]() {
    return createIterator(3);
  },
};
console.log([...iterable]); // [0,1,2]
```
