# #428 「実践例」

四国めたん「Promise<void>の現場的な例を見てみましょう。」
ずんだもん「updateProfileはfetchしてログを出すだけだった。」
四国めたん「はい。結果を返さないAPI呼び出しです。」
ずんだもん「processBatchはfor-ofで順番にprocessItemをawaitしてたね。」
四国めたん「実務でもよくあるパターンです。」
ずんだもん「initializeAppはloadConfigやstartServicesを順番にawaitしてた!」
四国めたん「アプリ起動時の副作用にもPromise<void>が役立ちます。」
ずんだもん「現実のユースケースを参考に設計するのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: API呼び出し */
async function updateProfile(profile: Profile): Promise<void> {
  await fetch("/api/profile", {
    method: "PUT",
    body: JSON.stringify(profile)
  });
  console.log("Profile updated");
}

/** Example 2: バッチ処理 */
async function processBatch(items: Item[]): Promise<void> {
  for (const item of items) {
    await processItem(item);
  }
  console.log("Batch complete");
}

/** Example 3: アプリ初期化 */
async function initializeApp(): Promise<void> {
  await loadConfig();
  await connectDatabase();
  await startServices();
  console.log("App initialized");
}
```
