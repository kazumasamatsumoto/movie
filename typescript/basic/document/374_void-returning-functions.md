# #374 「void型を返す関数」

四国めたん「voidを返す関数の振る舞いを確認しましょう。」
ずんだもん「log1のようにreturnを書かないのが基本なんだね!」
四国めたん「はい。でも条件付きでreturn; することもあります。」
ずんだもん「log2で値なしreturnしてもvoid扱いなんだ?」
四国めたん「そうです。早期終了しても型はvoidのままです。」
ずんだもん「return undefined; は許されるって本当?」
四国めたん「log3のようにundefinedを返してもコンパイラは許可します。」
ずんだもん「void関数のreturnルールを把握するのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: return文なし */
function log1(msg: string): void {
  console.log(msg);
}

/** Example 2: 値を指定しないreturn */
function log2(msg: string): void {
  if (!msg) return;
  console.log(msg);
}

/** Example 3: undefinedを返す */
function log3(msg: string): void {
  console.log(msg);
  return undefined;
}
```
