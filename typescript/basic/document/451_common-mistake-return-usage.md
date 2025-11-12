# #451 「間違い(1) - 戻り値使用」

四国めたん「void戻り値を使おうとするのは代表的な誤りです。」
ずんだもん「logの結果をstringに代入しようとして怒られたことがある!」
四国めたん「update() + 1 のように計算へ使うのもNGです。」
ずんだもん「解決策は戻り値を無視して副作用だけ呼び出すこと?」
四国めたん「はい。process(); と書いて結果を使わないのが正解です。」
ずんだもん「voidを見たら『戻り値を触らない』と覚えておくのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 間違い: 戻り値を使用 */
function log(msg: string): void {
  console.log(msg);
}
const result: string = log("Hello");

/** Example 2: 間違い: 計算に利用 */
function update(): void {
  count++;
}
const value = update() + 1;

/** Example 3: 正しい使い方 */
function process(): void {
  doSomething();
}
process();
console.log("Done");
```
