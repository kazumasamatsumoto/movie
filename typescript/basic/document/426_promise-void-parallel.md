# #426 「並行実行」

四国めたん「Promise.all()でPromise<void>を並行実行できます。」
ずんだもん「processAllはsaveUserを3つ同時に待ってたね。」
四国めたん「はい。全て終わるまでawaitします。」
ずんだもん「initializeもloadConfigやconnectDatabaseを並行で走らせてる!」
四国めたん「重い初期化を短縮できます。」
ずんだもん「Promise.allの中でエラーが起きたらcatchで拾うの?」
四国めたん「processWithErrorのようにtry-catchでまとめて処理します。」
ずんだもん「並行実行で効率よく副作用をこなすのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: Promise.all()で並行 */
async function processAll(): Promise<void> {
  await Promise.all([
    saveUser(user1),
    saveUser(user2),
    saveUser(user3)
  ]);
  console.log("All saved");
}

/** Example 2: 初期化 */
async function initialize(): Promise<void> {
  await Promise.all([
    loadConfig(),
    connectDatabase(),
    startCache()
  ]);
}

/** Example 3: エラーハンドリング */
async function processWithError(): Promise<void> {
  try {
    await Promise.all([task1(), task2(), task3()]);
  } catch (error) {
    console.error("One of the tasks failed:", error);
  }
}
```
