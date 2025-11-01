# #780 「Symbol.asyncIterator」

四国めたん「Symbol.asyncIteratorは非同期イテレータを提供します。」
ずんだもん「for await...ofで使えるようになるんだよね。」
四国めたん「Promiseを返すnext()を実装するか、asyncジェネレータを使います。」
ずんだもん「あいまいなポーリング処理を整えられそうだよ。」
四国めたん「TypeScriptではAsyncIterator<T>を返すメソッドとして型付けします。」
ずんだもん「非同期ストリームを抽象化するのに便利だね。」
四国めたん「Symbol.asyncIteratorを活用して非同期処理をコントロールしましょう。」
ずんだもん「リアクティブプログラミングにも応用できるよ！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: asyncジェネレータ */
const ticker = {
  async *[Symbol.asyncIterator]() {
    let count = 0;
    while (count < 3) {
      await new Promise((resolve) => setTimeout(resolve, 10));
      yield count++;
    }
  },
};

/** Example 2: for await...of */
(async () => {
  for await (const value of ticker) {
    console.log("tick", value);
  }
})();

/** Example 3: AsyncIterator型 */
const stream: AsyncIterator<number> = ticker[Symbol.asyncIterator]();
stream.next().then(console.log);
```
