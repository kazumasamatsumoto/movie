# #465 「never型の宣言」

四国めたん「never型は主に関数の戻り値で宣言します。」
ずんだもん「throwError(message): never が基本形だね。」
四国めたん「変数にneverを付けることは稀で、代入は禁止されます。」
ずんだもん「throwするだけの関数は型推論でもneverになる?」
四国めたん「はい。fail関数のようにreturnしなければ自動でneverです。」
ずんだもん「宣言と推論を使い分けるのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 関数で宣言 */
function throwError(message: string): never {
  throw new Error(message);
}

/** Example 2: 変数で宣言 */
let neverValue: never;
// neverValue = 1;

/** Example 3: 型推論 */
function fail(msg: string) {
  throw new Error(msg);
}
```
