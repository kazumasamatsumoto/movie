# #419 「使用例」

四国めたん「Promise<void>の代表的な使用例を見てみましょう。」
ずんだもん「saveDataは保存してログを残すだけだったね。」
四国めたん「はい。initializeでは設定や接続を待って完了を知らせます。」
ずんだもん「cleanupもリソースを閉じて終わりだ!」
四国めたん「結果を返す必要がなく、完了だけ伝えたい場面で使います。」
ずんだもん「実践例を押さえてPromise<void>を自信を持って使うのだ!」
四国めたん「副作用系のasync処理にはぴったりです。」

---

## 📺 画面表示用コード

```typescript
/** Example 1: データ保存 */
async function saveData(data: Data): Promise<void> {
  await database.save(data);
  await logActivity("Data saved");
}

/** Example 2: 初期化 */
async function initialize(): Promise<void> {
  await loadConfig();
  await connectDatabase();
  await startServer();
  console.log("Initialized");
}

/** Example 3: クリーンアップ */
async function cleanup(): Promise<void> {
  await closeConnections();
  await flushLogs();
  console.log("Cleanup complete");
}
```
