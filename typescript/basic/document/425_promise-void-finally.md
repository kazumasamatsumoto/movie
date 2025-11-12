# #425 「finally()」

四国めたん「finallyは成功・失敗に関わらず実行されます。」
ずんだもん「saveData().finally(() => Cleanup) のように書けたね。」
四国めたん「はい。async/awaitでもtry-catch-finallyで同じことができます。」
ずんだもん「ロード中の表示を制御する例もあった!」
四国めたん「loadDataではshowLoading→fetch→hideLoadingを必ず実行します。」
ずんだもん「finallyを使うと片付け処理を確実に走らせられるんだね。」
四国めたん「Promise<void>でも重要な保険になります。」
ずんだもん「必ず実行したい処理はfinallyに入れるのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: finally()メソッド */
saveData(data)
  .then(() => console.log("Success"))
  .catch((error) => console.error(error))
  .finally(() => {
    console.log("Cleanup");
  });

/** Example 2: async/awaitでのfinally */
async function process(): Promise<void> {
  try {
    await saveData(data);
  } catch (error) {
    console.error(error);
  } finally {
    await cleanup();
  }
}

/** Example 3: ローディング表示 */
async function loadData(): Promise<void> {
  showLoading();
  try {
    await fetchData();
  } finally {
    hideLoading();
  }
}
```
