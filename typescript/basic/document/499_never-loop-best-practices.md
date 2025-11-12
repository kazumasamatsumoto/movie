# #499 「ベストプラクティス」

四国めたん「無限ループを書くときのベストプラクティスを押さえましょう。」
ずんだもん「serverLoop()ではログを出していたね。」
四国めたん「safeLoop()はtry-catchと待機を組み合わせていました。」
ずんだもん「gracefulLoop()は終了シグナルで抜ける仕組みがあった!」
四国めたん「シグナル処理やエラーハンドリングを忘れないでください。」

---

## 📺 画面表示用コード

```typescript
/** Example 1: ログ付きループ */
function serverLoop(): never {
  console.log("Server started");
  while (true) {
    const request = waitForRequest();
    handleRequest(request);
  }
}

/** Example 2: エラーハンドリング */
async function safeLoop(): never {
  while (true) {
    try {
      await processTask();
    } catch (error) {
      console.error("Error:", error);
    }
    await delay(1000);
  }
}

/** Example 3: 終了シグナル */
let shouldRun = true;
function gracefulLoop(): void {
  while (shouldRun) {
    doWork();
  }
  cleanup();
}
process.on('SIGTERM', () => { shouldRun = false; });
```
