# #421 「await」

四国めたん「awaitでPromise<void>の完了を待ちましょう。」
ずんだもん「processではsaveDataとlogActivityを順番にawaitしてたね。」
四国めたん「はい。各処理が終わるまで先に進みません。」
ずんだもん「await式の型はvoidだから代入しても使わないんだ?」
四国めたん「その通り。result: void = await initialize(); のように扱います。」
ずんだもん「step1→step2→step3のように順番実行したいときに便利!」
四国めたん「awaitを挟めば読みやすい直列フローが書けます。」
ずんだもん「async処理を直感的に書くためにawaitを活用するのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: awaitで完了を待つ */
async function process(): Promise<void> {
  await saveData(data);
  await logActivity("Saved");
  console.log("All done");
}

/** Example 2: await式の型はvoid */
async function example(): Promise<void> {
  const result: void = await initialize();
}

/** Example 3: 順次実行 */
async function sequence(): Promise<void> {
  await step1();
  await step2();
  await step3();
}
```
