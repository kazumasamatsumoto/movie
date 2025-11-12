# #461 「never型とは」

四国めたん「never型は『絶対に戻ってこない』ことを表します。」
ずんだもん「throw Error する関数が典型なんだね。」
四国めたん「無限ループもneverになります。」
ずんだもん「voidとの違いは制御が戻るか戻らないか?」
四国めたん「はい。voidは実行後に次の行へ進みますがneverは終了しません。」
ずんだもん「危険な処理を型で宣言できるのは安心だね。」
四国めたん「neverで『ここには到達しない』と示しましょう。」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 例外を投げる */
function throwError(message: string): never {
  throw new Error(message);
}

/** Example 2: 無限ループ */
function infiniteLoop(): never {
  while (true) {
    console.log("Running...");
  }
}

/** Example 3: voidとの違い */
function voidFunc(): void {
  console.log("Done");
}
function neverFunc(): never {
  throw new Error("Never returns");
}
```
