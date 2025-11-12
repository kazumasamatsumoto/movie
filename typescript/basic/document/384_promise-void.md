# #384 「Promise<void>」

四国めたん「非同期処理でもvoidを使う場面があります。」
ずんだもん「async function saveData(...): Promise<void> がその例だね。」
四国めたん「はい。保存が終わったことだけを伝えたいときに使います。」
ずんだもん「async function initialize() みたいに推論でPromise<void>になるのも便利。」
四国めたん「その通り。returnが無ければPromise<void>として扱われます。」
ずんだもん「processAllではPromise.allをawaitして完了メッセージを出してる!」
四国めたん「複数処理をまとめて走らせるときも、戻り値が不要ならPromise<void>が最適です。」
ずんだもん「非同期副作用でもvoidを意識するのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: Promise<void>の基本 */
async function saveData(data: Data): Promise<void> {
  await database.save(data);
  console.log("Saved");
}

/** Example 2: 推論でPromise<void> */
async function initialize() {
  await loadConfig();
  await connectDB();
  // Promise<void>と推論される
}

/** Example 3: 実用例 */
async function processAll(items: Item[]): Promise<void> {
  await Promise.all(items.map(item => saveItem(item)));
  console.log("All items processed");
}
```
