# #427 「Promise.all()」

四国めたん「Promise.all()の戻り値も理解しておきましょう。」
ずんだもん「saveAllのresultsはvoid[] で実際には使ってなかったね。」
四国めたん「はい。全てundefinedなので配列を無視します。」
ずんだもん「Promise.allSettled()なら成功/失敗を確認できる?」
四国めたん「resultsを見てrejectedだけログする例がありました。」
ずんだもん「Promise.race()でタイムアウトを実装するテクもあった!」
四国めたん「longTaskとdelayを競わせて先に終わった方を採用します。」
ずんだもん「便利なPromiseユーティリティを使い分けるのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: Promise.all()の戻り値 */
async function saveAll(): Promise<void> {
  const results: void[] = await Promise.all([
    saveData(data1),
    saveData(data2),
    saveData(data3)
  ]);
}

/** Example 2: Promise.allSettled() */
async function processAllSettled(): Promise<void> {
  const results = await Promise.allSettled([task1(), task2(), task3()]);
  results.forEach((result) => {
    if (result.status === "rejected") {
      console.error(result.reason);
    }
  });
}

/** Example 3: Promise.race() */
async function timeout(): Promise<void> {
  await Promise.race([
    longTask(),
    delay(5000).then(() => { throw new Error("Timeout"); })
  ]);
}
```
