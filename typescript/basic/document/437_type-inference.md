# #437 「型推論」

四国めたん「型推論でもvoidが導かれます。」
ずんだもん「execute(() => console.log()) の戻り値がvoidと推論されてたね。」
四国めたん「はい。PromiseでもawaitしていなければPromise<void>と推論されます。」
ずんだもん「必要ならexecute<void>(() => ...) みたいに型を指定できる?」
四国めたん「もちろんです。」
ずんだもん「推論と明示を使い分けるのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 型推論でvoid */

function execute<T>(fn: () => T): T {
  return fn();
}
const result = execute(() => {
  console.log("Done");
});

/** Example 2: Promiseの型推論 */

async function process() {
  await doSomething();
}

/** Example 3: 明示的な型指定 */

const result2 = execute<void>(() => {
  console.log("Done");
});
```
