# #387 「console.logの戻り値」

四国めたん「console.logもvoidを返す関数です。」
ずんだもん「result = console.log("Hello"); とするとresultはvoid型なんだね。」
四国めたん「はい。戻り値を他の値に代入して使う設計ではありません。」
ずんだもん「logAndReturnでconsole.logの戻り値をstringとして返そうとするとエラー?」
四国めたん「そうです。Type 'void' is not assignable to type 'string' と怒られます。」
ずんだもん「processではconsole.logを呼ぶだけで、副作用関数として正しく使ってるんだね。」
四国めたん「console.logは副作用専用だと覚えておきましょう。」
ずんだもん「戻り値がvoidなAPIを誤用しないのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: console.logの型 */
const result = console.log("Hello");
// result: void型

/** Example 2: 戻り値を使うべきでない */
function logAndReturn(msg: string): string {
  return console.log(msg);  // エラー
}

/** Example 3: 正しい使い方 */
function process(data: Data): void {
  console.log("Processing:", data);
}
```
