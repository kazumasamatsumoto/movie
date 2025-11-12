# #422 「await式の型」

四国めたん「await式の型はPromiseの中身に依存します。」
ずんだもん「saveDataをawaitするとvoidになるんだね。」
四国めたん「はい。result: void に代入しても何も使いません。」
ずんだもん「Promise.resolve(42)をawaitするとnumberになる?」
四国めたん「その通り。voidとTで挙動が違います。」
ずんだもん「resultをstringに代入しようとするとエラーが出るんだ。」
四国めたん「型がvoidなので別の型へ代入できません。」
ずんだもん「await式の型を理解して安全に扱うのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: await式の型 */
async function example(): Promise<void> {
  const result: void = await saveData(data);
}

/** Example 2: Promise<T>との比較 */
async function compare(): Promise<void> {
  const num: number = await Promise.resolve(42);
  const v: void = await Promise.resolve();
}

/** Example 3: 値として使えない */
async function invalid(): Promise<void> {
  const result = await initialize();
  // const str: string = result;
}
```
