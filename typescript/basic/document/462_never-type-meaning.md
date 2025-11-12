# #462 「never型の意味」

四国めたん「neverは『この先へ進まない』ことを明示します。」
ずんだもん「fail関数が例外を投げて処理を止めていたね。」
四国めたん「サーバーのメインループのように永遠に続く処理もneverです。」
ずんだもん「switchで全ケースを処理したか確認するのにも使える?」
四国めたん「はい。最後にfail("Unreachable")を呼べば型が保証されます。」
ずんだもん「neverで型チェックと実行フローの両方を管理できるんだ。」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 例外で停止 */
function fail(message: string): never {
  throw new Error(message);
}

/** Example 2: 無限ループ */
function serve(): never {
  while (true) {
    handleRequest();
  }
}

/** Example 3: 到達不可能性 */
function process(value: string | number): string {
  if (typeof value === "string") {
    return value.toUpperCase();
  } else if (typeof value === "number") {
    return value.toString();
  }
  return fail("Unreachable");
}
```
