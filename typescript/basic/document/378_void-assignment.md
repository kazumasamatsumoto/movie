# #378 「変数への代入」

四国めたん「void型変数に代入できる値を確認しましょう。」
ずんだもん「value: void にはundefinedだけが代入可能なんだね。」
四国めたん「はい。nullや数値を入れると型エラーになります。」
ずんだもん「サンプルではコメントアウトでエラー例が示されていたね。」
四国めたん「strictNullChecksでは特に注意が必要です。」
ずんだもん「voidを返す関数の戻り値を代入するとundefinedになる?」
四国めたん「doSomething(): void を呼んでconst result: void = ...とすれば型整合します。」
ずんだもん「代入ルールを理解して想定外のエラーを防ぐのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 代入可能な値 */
let value: void;
value = undefined;  // OK

/** Example 2: エラー例 */
let value: void;
// value = null;       // strictNullChecks有効時はエラー
// value = 0;          // エラー
// value = "string";   // エラー

/** Example 3: void関数の戻り値 */
function doSomething(): void {
  console.log("Done");
}
const result: void = doSomething();  // undefined
```
