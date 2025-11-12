# #423 「Promise<void>の連鎖」

四国めたん「Promise<void>はthen()を連鎖させて処理できます。」
ずんだもん「saveData().then(...).then(...) のコードがあったね。」
四国めたん「はい。エラーはcatchでまとめて扱えます。」
ずんだもん「async/awaitで書き直すと読みやすい?」
四国めたん「process関数のようにawaitを並べれば直列になります。」
ずんだもん「initialize().then(...).then(...); もPromise<void>型なんだね。」
四国めたん「連鎖結果全体がPromise<void>になります。」
ずんだもん「状況に応じてthen連鎖とawaitを使い分けるのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: Promise<void>の連鎖 */
saveData(data)
  .then(() => logActivity("Saved"))
  .then(() => notify("Complete"))
  .catch((error) => console.error(error));

/** Example 2: async/await版 */
async function process(): Promise<void> {
  await saveData(data);
  await logActivity("Saved");
  await notify("Complete");
}

/** Example 3: 連鎖の型 */
const promise: Promise<void> = initialize()
  .then(() => loadData())
  .then(() => render());
```
