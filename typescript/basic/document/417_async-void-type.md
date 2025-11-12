# #417 「async関数のvoid型」

四国めたん「async関数の戻り値は必ずPromise型になります。」
ずんだもん「process(): Promise<void> が正しい書き方だったね。」
四国めたん「はい。async function process(): void はエラーです。」
ずんだもん「型推論に任せてasync function load() {} と書くのもアリ?」
四国めたん「returnが無ければPromise<void>と推論されます。」
ずんだもん「void型を意識しつつPromiseで包む必要があるんだね。」
四国めたん「async関数では常にPromise<void>を意識しましょう。」
ずんだもん「正しい宣言でasync void関数を書き上げるのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 正しい書き方 */
async function process(): Promise<void> {
  await doSomething();
  console.log("Done");
}

/** Example 2: エラー例 */
// async function process(): void {
//   await doSomething();
// }

/** Example 3: 型推論 */
async function load() {
  await fetch("/api/data");
}
```
