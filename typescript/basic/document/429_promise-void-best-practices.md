# #429 「ベストプラクティス」

四国めたん「Promise<void>を書くときのベストプラクティスを確認しましょう。」
ずんだもん「型注釈を明示するのが第一だね。」
四国めたん「はい。saveData(data): Promise<void> のように書きます。」
ずんだもん「エラーハンドリングも重要!」
四国めたん「processではtry-catch-finallyで異常系を網羅しました。」
ずんだもん「並行実行にはPromise.allを活用するんだね。」
四国めたん「processAllのようにmap + Promise.allで効率化できます。」
ずんだもん「ベストプラクティスを守って安心してPromise<void>を書くのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 明示的な型 */
async function saveData(data: Data): Promise<void> {
  await database.save(data);
}

/** Example 2: エラーハンドリング */
async function process(): Promise<void> {
  try {
    await processData();
  } catch (error) {
    console.error("Failed:", error);
    throw error;
  } finally {
    await cleanup();
  }
}

/** Example 3: 並行実行 */
async function processAll(items: Item[]): Promise<void> {
  await Promise.all(items.map(item => saveItem(item)));
}
```
