# #420 「then() - 引数なし」

四国めたん「Promise<void>はthen()で完了ハンドラを登録できます。」
ずんだもん「saveData(data).then(() => ...) の例があったね。」
四国めたん「はい。引数なしのコールバックで完了を処理します。」
ずんだもん「initialize().then(() => ...).catch(...) のようにチェーンもできる?」
四国めたん「もちろんです。」
ずんだもん「でもasync/awaitの方が読みやすい場面もあるんだね。」
四国めたん「main関数でawaitを使えば同期的に書けます。」
ずんだもん「thenとawaitを状況に応じて使い分けるのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: then()で完了を待つ */
saveData(data).then(() => {
  console.log("Save complete");
});

/** Example 2: チェーンとエラーハンドリング */
initialize().then(() => {
  console.log("Initialized");
}).catch((error) => {
  console.error("Failed:", error);
});

/** Example 3: async/await */
async function main() {
  await saveData(data);
  console.log("Save complete");
}
```
