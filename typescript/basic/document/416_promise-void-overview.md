# #416 「Promise<void>とは」

四国めたん「非同期処理でもvoidを使う場面があります。」
ずんだもん「saveDataはPromise<void>を返してたね。」
四国めたん「はい。完了したことだけ伝えたいときに使います。」
ずんだもん「async function initialize() みたいに型推論でもPromise<void>になる?」
四国めたん「returnが無ければ自動でPromise<void>になります。」
ずんだもん「mainでもPromise<void>を返してログを出してた!」
四国めたん「副作用主体のasync関数ではPromise<void>が適しています。」
ずんだもん「非同期でもvoidの考え方を適用するのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: Promise<void>の基本 */
async function saveData(data: Data): Promise<void> {
  await database.save(data);
  console.log("Saved");
}

/** Example 2: 型推論 */
async function initialize() {
  await loadConfig();
  await connectDB();
}

/** Example 3: 使用例 */
async function main(): Promise<void> {
  await saveData({ id: 1, name: "Alice" });
  console.log("Complete");
}
```
