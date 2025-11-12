# #430 「非同期voidまとめ」

四国めたん「Promise<void>のポイントを総まとめしましょう。」
ずんだもん「saveDataのように副作用だけして完了を知らせるんだね。」
四国めたん「はい。awaitで順次処理を書けます。」
ずんだもん「processAllではPromise.allで並行実行していた!」
四国めたん「複数タスクをまとめて待つときに便利です。」
ずんだもん「非同期void関数の設計思想が固まった気がするよ。」
四国めたん「副作用、await、並行実行の3点を押さえておきましょう。」
ずんだもん「まとめを胸にPromise<void>を使いこなすのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: Promise<void>の基本 */
async function saveData(data: Data): Promise<void> {
  await database.save(data);
  console.log("Saved");
}

/** Example 2: awaitで完了を待つ */
async function process(): Promise<void> {
  await saveData(data);
  await logActivity("Complete");
}

/** Example 3: 並行実行 */
async function processAll(): Promise<void> {
  await Promise.all([task1(), task2(), task3()]);
  console.log("All complete");
}
```
